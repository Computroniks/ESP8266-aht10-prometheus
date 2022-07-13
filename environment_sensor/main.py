"""
Main entrypoint for 
"""

import sys

from .utils import initWLAN, readSettings
from .HTTP import HTTP

def main() -> None:
    
    settings = readSettings()
    if not initWLAN(settings["SSID"], settings["KEY"], settings["TIMEOUT"], settings["STATIC"], settings["ADDR"], settings["MASK"], settings["GATEWAY"]):
        print("ERROR Could not connect to Wi-Fi network")
        sys.exit(1)

    # server = initHTTPServer(int(settings["PORT"]), int(settings["MAX_CON"]), settings["ADDR_FAMILY"])
    # listen(server)
    server = HTTP(settings["PORT"], settings["MAX_CON"], settings["ADDR_FAMILY"])
    server.listen()