"""
System Security Check
Author: Vincent Anany

A simple Python automation script for collecting
basic system information for security review.
"""

import platform
import socket
import os


def system_information():
    print("=== System Security Check ===")
    print(f"Hostname: {socket.gethostname()}")
    print(f"Operating System: {platform.system()}")
    print(f"OS Version: {platform.version()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Current User: {os.getenv('USERNAME') or os.getenv('USER')}")


if __name__ == "__main__":
    system_information()
