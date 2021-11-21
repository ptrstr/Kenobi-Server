# Key emulating class 

from pynput.keyboard import Key, Controller
from os import system

class KeyController:
    """
    Class which emulates a key presses, controls media playback
    """
    def __init__(self):
        """
        Initialize the key controller
        And valid key dictionaries
        """
        self.keyboard = Controller()
        self.vaildKeys = {
            "left": Key.left,
            "right": Key.right,
            "up": Key.up,
            "down": Key.down,
            "space": Key.space,
            "tab": Key.tab,
            "return": Key.enter,
            "escape": Key.esc,
            "playpause": Key.media_play_pause,
            "next": Key.media_next,
            "previous": Key.media_previous,
            "mute": Key.media_volume_mute,
            "volumeup": Key.media_volume_up,
            "volumedown": Key.media_volume_down
        }
    
    def emulate_key(self, recievedKey: str):
        """
        Check if the key is valid, and if so
        Emulate the key using the keyboard controller
        """
        if recievedKey in self.vaildKeys:
            self.keyboard.press(self.vaildKeys[recievedKey])
        else:
            # TODO: Add error handling
            system("echo 'Key not found'")
    

    
if __name__ == "__main__":
    key = KeyController()
    key.emulate_key("volumeUp")