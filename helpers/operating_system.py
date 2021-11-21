""""
Find out what operating system is running.
"""

import platform

from custom_logger import CustomLogger


class OperatingSystem:
    """
    Find out what operating system is running.
    """
    def __init__(self) -> None:
        self.logger = CustomLogger("OperatingSystem")
        self.os = platform.system()
        self.is_supported_os()

    def is_supported_os(self):
        """
        Check if the operating system is any OS.
        """
        if not(self.os == "Darwin" or self.os == "Linux" or self.os == "Windows"):
            self.logger.error("Operating system is not supported.")

    def is_mac(self) -> bool:
        """
        Check if the operating system is Mac.
        """
        return self.os == "Darwin"
    
    def is_windows(self) -> bool:
        """
        Check if the operating system is Windows.
        """
        return self.os == "Windows"
    
    def is_linux(self) -> bool:
        """
        Check if the operating system is Linux.
        """
        return self.os == "Linux"
    