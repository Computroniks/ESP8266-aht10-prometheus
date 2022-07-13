"""
Main entrypoint for 
"""

import sys

from .lib.micropython_ahtx0 import axth0
from machine import Pin, I2C

from .utils import initWLAN, readSettings
from .HTTP import HTTP
from .logging import debug, info, warn, error, fatal


def main() -> None:
    
    settings = readSettings()
    if not initWLAN(settings["SSID"], settings["KEY"], settings["TIMEOUT"], settings["STATIC"], settings["ADDR"], settings["MASK"], settings["GATEWAY"]):
        print("ERROR Could not connect to Wi-Fi network")
        sys.exit(1)
    
    i2c = I2C(scl = Pin(0), sda = Pin(2))
    sensor = axth0.AHT10(i2c)

    server = HTTP(sensor, settings["PORT"], settings["MAX_CON"], settings["ADDR_FAMILY"])
    server.listen()