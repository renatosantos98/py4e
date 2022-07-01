# Exercise 3: Use urllib to replicate the previous exercise of
# (1) retrieving the document from a URL,
# (2) displaying up to 3000 characters, and
# (3) counting the overall number of characters in the document.
# Don't worry about the headers for this exercise, simply show the first 3000 characters of the document contents.

import urllib.request, urllib.parse, urllib.error

try:
    url = input("Enter a URL: ")
    file = urllib.request.urlopen(url)
    words = ""
    for line in file:
        words += line.decode().rstrip()
    words = words[:3000]
    print(words)
    print("Number of characters: ", len(words))
except:
    print("Error: Invalid URL")
