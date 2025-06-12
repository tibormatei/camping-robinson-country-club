# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: main.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

from http.server import ThreadingHTTPServer
from CampingRobinsonCountryClubServer import CampingRobinsonCountryClubServer


if __name__ == "__main__":
    HOST_NAME = "localhost"
    SERVER_PORT = 8080

    print('Server starting ...')

    webServer = ThreadingHTTPServer((HOST_NAME, SERVER_PORT), CampingRobinsonCountryClubServer)
    print(f"Server started http://{HOST_NAME}:{SERVER_PORT}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped!")
