# ESP8266 Environment Monitor

A ESP8266 environment monitor designed to provide a convenient
Prometheus interface allowing it to intergrate with existing monitoring
infrastructure.

## Deployment

To deploy clone this repository then create the following files:
`.ampy` - This configures various ampy settings. You may need to alter
these to suit your environment

```
AMPY_PORT=/dev/ttyUSB0
```

`settings.txt`
This allows you to configure the sensor to suit your network. A list of
all options can be found later in this document but the example below
should give you basic functionality.

```
SSID=<your SSID>
KEY=<your key>
```

You should then create a python virtual environment and install ampy
using the following command.

```
pip install adafruit-ampy
```

You will also require GNU Make if you want to make use of automated
uploads.

To upload the code to the board, run `make` in the root of the
repository. This will upload all of the files to the board correctly.

## Settings

Settings are stored in the settings.txt file and use the following
format:
```
<SETTING NAME>=<SETTING VALUE>
```

A table of all settings can be found below:

| Setting | Required? | Description | Type | Default |
| --- | --- | --- | --- | --- |
| SSID | Yes | The SSID of the WLAN to connect to | string | None |
| KEY | Yes | Key to use to connect to WLAN | string | None |
| MAX_CON | No | Maximum number of connections to accept to HTTP server | integer | 5 |
| TIMEOUT | No | Timeout to use when connecting to WLAN | integer | 10 |
| PORT | No | Port to start HTTP server on | integer | 80 |
| STATIC | No | Should a static IP be used? One of `TRUE`or `FALSE` | boolean | FALSE |
| ADDR | Only if `STATIC=TRUE` | Static IP to use | string | None |
| MASK | Only if `STATIC=TRUE` | Subnet mask to use | string | None |
| GATEWAY | Only if `STATIC=TRUE` | Default gateway to use | string | None |
| ADDR_FAMILY | Only if `STATIC=TRUE` | Address family to use for HTTP server. One of `INET` or `INET6` | string | None |

## Licence

The majority of this software is licenced under the MIT licence which
can be found in the root of this repository. However, any files in the
`environment_sensor/libs` directory may fall under a different licence.
All files here have been installed using PIP and licensing information
can be found in the directory `<package name>-<version>.dist-info`.
These are third party libraries that are used by this project.
