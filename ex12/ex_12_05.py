# Exercise 5: (Advanced) Change the socket program so that it only shows data after the headers and a blank line have been received.
# Remember that recv is receiving characters (newlines and all), not lines.

import socket

url = input("Enter a URL: ")
try:
    host = url.split("/")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host[2], 80))
    cmd = ("GET " + url + " HTTP/1.0\r\n\r\n").encode()
    sock.send(cmd)

    data_received = ""

    while True:
        data = sock.recv(512)
        if len(data) < 1:
            break
        data_received += data.decode()

except:
    print("Error: Invalid URL")

pos = data_received.find("\r\n\r\n")
content = data_received[pos + 4 :]
print(content)

sock.close()
