"""
Main application file with the main function.
And argument parser.
"""
import asyncio
from argparse import ArgumentParser

from helpers.websocket_server import WebsocketServer


class Main:
    """
    Class Main which contains the main function.
    And argument parser.
    """

    def __init__(self) -> None:
        """
        Initialize the main class.
        """
        self.debug = False
        self.background = True
        self.main()

    @staticmethod
    def parser():
        """
        Parse the arguments.
        Arguments:
            Run in background:
                -b, --background
            Run in debug mode:
                -d, --debug
        """
        parser = ArgumentParser(description="Kenobi Server")
        # add --background and --debug flags default to False

        parser.add_argument("-b", "--background", action="store_true",
                            help="Run in background")
        parser.add_argument("-d", "--debug", action="store_true",
                            default=False, help="Run in debug mode")
        return parser.parse_args()

    def main(self):
        """
        Main function.
        """
        args = self.parser()
        if args.background:
            self.background = True
        if args.debug:
            self.debug = True

        WebsocketServer(debug=self.debug)
        asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    Main()
