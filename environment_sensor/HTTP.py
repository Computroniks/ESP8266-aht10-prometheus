import socket
import time

from .logging import debug, info, warn, error, fatal


class HTTP:
    def __init__(self, port: int, max_con: int, addr_family: str = "INET")  -> None:
        """
        __init__ Initialize the web server

        Initialize the TCP socket to listen on the specified port with the
        specified maximum number of connections.

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

        info("Network", "Initializing HTTP server")

        if addr_family == "INET":
            family = socket.AF_INET
        elif addr_family == "INET6":
            family = socket.AF_INET6

        self._s = socket.socket(family, socket.SOCK_STREAM)
        self._s.bind(('', port))
        self._s.listen(max_con)

        info("Network", "HTTP server initialized")

    def listen(self) -> None:
        """
        listen Listen and respond to HTTP requests
        """

        info("Network", "Waiting for requests")

        while True:
            conn, addr = self._s.accept()
            info("Network", "Got connection from {}".format(addr))

            conn.send("HTTP/1.1 200 OK\n")
            conn.send("Content-Type: text/plain\n")
            conn.send("Connection: close\n\n")
            # Just send current time for testing
            conn.send(str(time.time()))
            conn.close()