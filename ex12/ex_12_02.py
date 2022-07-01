# Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters.
# The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document.

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
    data_received = data_received[:3000]
    count = len(data_received)
    print("Number of characters: ", count)

    sock.close()

except:
    print("Error: Invalid URL")
