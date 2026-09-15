#!/usr/bin/env python3
"""🐙 Cyclopus container healthcheck."""
import sys
import socket

def check_port(host: str, port: int, timeout: float = 3.0) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False

def main() -> int:
    # Web dashboard
    if not check_port("127.0.0.1", 5000):
        print("Web dashboard not responding on port 5000")
        return 1
    print("✅ Cyclopus healthy")
    return 0

if __name__ == "__main__":
    sys.exit(main())