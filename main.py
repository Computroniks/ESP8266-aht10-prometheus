"""
Main entrypoint for ESP8266 based environment monitor
"""

import gc

import environment_sensor

if __name__ == "__main__":
    gc.collect()

    environment_sensor.main()