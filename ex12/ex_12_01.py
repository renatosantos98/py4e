# Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page.
# You can use split('/') to break the URL into its component parts so you can extract the host name for the socket connect call.
# Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL.

import socket

url = str(input("Enter a URL: "))
try:
    host = url.split("/")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host[2], 80))
    cmd = ("GET " + url + " HTTP/1.0\r\n\r\n").encode()
    sock.send(cmd)

    while True:
        data = sock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end="")

    sock.close()
except:
    print("Error: Invalid URL")
