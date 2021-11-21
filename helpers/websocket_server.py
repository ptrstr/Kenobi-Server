"""
Webserver for the the client to connect to
"""

import asyncio

import websockets

from message_parser import MessageParser as mp


class WebsocketServer:
    """
    Class for handling the websocket server and executing the commands
    """
    def __init__(self) -> None:
        self.parser = mp()
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
        print(f"Starting Websocket server...@ {self.host}:{self.port}")
        self.server = await websockets.serve(self.handler, self.host, self.port)

    async def handler(self, websocket) -> None:
        """
        Handle the websocket connection, and receive messages
        """
        self.connected = True
        self.connected_ip = websocket.remote_address[0]
        self.connected_port = websocket.remote_address[1]
        if self.connected:
            pass
        else:
            print(f"Websocket connected from {self.connected_ip}:{self.connected_port}")
        while True:
            try:
                message = await websocket.recv()
                try:
                    key, value = self.parser.parse(message)
                    print(f"Parsed: {key}:{value}")
                except ValueError as error:
                    # print(f"Error: {error}")
                    print("...")
            except websockets.exceptions.ConnectionClosed:
                print("Websocket connection closed")
                self.connected = False
                self.connected_ip = None
                self.connected_port = None
                break

if __name__ == "__main__":
    server = WebsocketServer()
    asyncio.get_event_loop().run_forever()
