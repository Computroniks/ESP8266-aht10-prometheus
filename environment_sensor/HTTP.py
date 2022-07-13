try:
    import usocket as socket
except:
    import socket

from .lib.micropython_ahtx0 import axth0

from .logging import debug, info, warn, error, fatal

CONTENT = """
Content-Type: text/plain
Connection: keep-alive
Keep-Alive: timeout=5, max=1000
Content-Length: {}

{}
"""
class HTTP:
    def __init__(self, sensor: axth0.AHT10, port: int, max_con: int, addr_family: str = "INET")  -> None:
        """
        __init__ Initialize the web server

        Initialize the TCP socket to listen on the specified port with the
        specified maximum number of connections.

        :param sensor: Sensor to read from
        :type sensor: axth0.AHT10
        :param port: Port to bind to
        :type port: int
        :param max_con: Maximum number of concurrent connections
        :type max_con: int
        :param addr_family: Address family to use. One of INET or INET6,
            defaults to INET
        :type addr_family: str, optional
        :return: Socket to listen on
        :rtype: socket
        """

        self._sensor = sensor

        info("Network", "Initializing HTTP server")

        if addr_family == "INET6":
            family = socket.AF_INET6
        else:
            family = socket.AF_INET

        self._s = socket.socket(family, socket.SOCK_STREAM)
        self._s.bind(('', port))
        self._s.listen(max_con)

        info("Network", "HTTP server initialized")

    def _craftResponse(self) -> str:
        """
        _craftResponse Craft the HTTP response

        Craft the body of the HTTP response in the Prometheus text format

        :return: Response
        :rtype: str
        """

        temp = self._sensor.temperature
        humidity = self._sensor.relative_humidity

        metrics = {
            "environment_temperature": {
                "help": "Current temperature read by sensor",
                "type": "gauge",
                "value": temp
            },
            "environment_humidity": {
                "help": "Current humidity read by sensor",
                "type": "gauge",
                "value": humidity
            }
        }

        res = ""
        for i in metrics:
            res += "# HELP {} {}\n".format(i, metrics[i]["help"])
            res += "# TYPE {} {}\n".format(i, metrics[i]["type"])
            res += "{} {}\n\n".format(i, metrics[i]["value"])

        return res
        

    def listen(self) -> None:
        """
        listen Listen and respond to HTTP requests
        """

        info("Network", "Waiting for requests")
        

        while True:
            conn, addr = self._s.accept()
            info("Network", "Got connection from {}".format(addr))

            res = self._craftResponse()
            conn.send("HTTP/1.1 200 OK")
            conn.send(CONTENT.format(len(res), res))
            debug("Network", "Sent: \n{}".format(CONTENT.format(len(res), res)))
            # conn.send(res)
            # debug("Network", "Sent:\n{}".format(res))
            debug("Network", "Finished sending body")
            conn.close()
            debug("Network", "Closed connection")