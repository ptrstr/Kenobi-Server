"""
Test file for the project.
"""

from src.message_parser import MessageParser


def test_parse_message_valid_message():
    """
    Test that a valid message is parsed correctly.
    """
    message = "Hello, World!"
    parser = MessageParser()
    parsed_message = parser.parse(message)
    assert parsed_message == "Hello, World!"
