"""
Webserver for the the client to connect to
"""

import asyncio

import websockets

from custom_logger import CustomLogger
from emulator import Emulator
from message_parser import MessageParser as mp


class WebsocketServer:
    """
    Class for handling the websocket server and executing the commands
    """
    def __init__(self, debug: bool = False) -> None:
        self.debug = debug

        self.parser = mp()
        self.emulator = Emulator()
        self.logger = CustomLogger("WebsocketServer")
        # Server settings (constants)
        self.host = "0.0.0.0"
        self.port = 9999
        # Client Info
        self.connected_ip = None
        self.connected_port = None
        # Server status
        self.connected = False
        # Start server
        asyncio.get_event_loop().run_until_complete(self.start())

    async def start(self) -> None:
        """
        Start the websocket server and listen for connections
        """
        self.logger.info(f"Starting websocket server @ {self.host}:{self.port}")
        self.server = await websockets.serve(self.handler, self.host, self.port)

    async def handler(self, websocket) -> None:
        """
        Handle the websocket connection, and receive messages
        """
        self.connected = True
        self.connected_ip = websocket.remote_address[0]
        self.connected_port = websocket.remote_address[1]
        self.logger.info(f"Client connected @ {self.connected_ip}:{self.connected_port}")

        while True:
            try:
                message = await websocket.recv()
                try:
                    key, value = self.parser.parse(message)
                    print(f"Parsed: {key}:{value}")
                    if key == "LAUNCHAPP":
                        self.emulator.launch_app(value)
                    elif key == "PING":
                        self.emulator.ping(value)
                    elif key == "SITE":
                        self.emulator.launch_site(value)
                    elif key == "POWER":
                        self.emulator.power_option(value)
                    elif key == "MEDIA" or key == "KEY":
                        self.emulator.emulate_key(key, value)
                    else:
                        self.logger.error(f"Invalid key: {key}")
                except ValueError as error:
                    self.logger.error(f"Invalid message: {error}")

            except websockets.exceptions.ConnectionClosed:
                self.logger.info(f"Client disconnected @ {self.connected_ip}:{self.connected_port}")
                self.connected = False
                self.connected_ip = None
                self.connected_port = None
                break

if __name__ == "__main__":
    server = WebsocketServer()
    asyncio.get_event_loop().run_forever()
