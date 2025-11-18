# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: main.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

from http.server import ThreadingHTTPServer
from camping_robinson_country_club_server import CampingRobinsonCountryClubServer


if __name__ == "__main__":
    HOST_NAME = "localhost"
    SERVER_PORT = 8080

    print('Server starting ...')

    web_server = ThreadingHTTPServer((HOST_NAME, SERVER_PORT), CampingRobinsonCountryClubServer)
    print(f"Server started http://{HOST_NAME}:{SERVER_PORT}")

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Server stopped!")
