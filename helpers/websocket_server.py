import websockets
import asyncio
from message_parser import MessageParser as mp


class WebsocketServer:
    def __init__(self) -> None:
        self.parser = mp()

        # Server settings (constants)
        self.host = "0.0.0.0"
        self.port = 9999

        # Client Info
        self.connectedIP = None
        self.connectedPort = None

        # Server status
        self.connected = False
        
        # Start server
        asyncio.get_event_loop().run_until_complete(self.start())
    
    async def start(self) -> None:
        print(f"Starting Websocket server...@ {self.host}:{self.port}")

        self.server = await websockets.serve(self.handler, self.host, self.port)

    async def handler(self, websocket: websockets.WebSocketServerProtocol, path: str) -> None:
        self.connected = True
        self.connectedIP = websocket.remote_address[0]
        self.connectedPort = websocket.remote_address[1]
        if self.connected:
            pass
        else:
            print(f"Websocket connected from {self.connectedIP}:{self.connectedPort}")
        while True:
            try:
                message = await websocket.recv()
                key, value = self.parser.parse(message)
                print(key, value)
                if key != None:
                    print(f"Websocket received: {key}  and {value}")
                else:
                    print(f"Invalid data received: {message}")

            except websockets.exceptions.ConnectionClosed:
                print(f"Websocket connection closed")
                self.connected = False
                self.connectedIP = None
                self.connectedPort = None
                break

    



if __name__ == "__main__":
    server = WebsocketServer()
    asyncio.get_event_loop().run_forever()