
# -*- coding: utf-8 -*-

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from helpers.message_parser import MessageParser




def test_exception():
    """
    Test if exceptions are thrown correctly
    """
    message = "Hello World!"
    parser = MessageParser()
    try:
        _ = parser.parse(message)
    except ValueError:
        assert True
    except:
        assert False
