# Exercise 1: Write a simple program to simulate the operation of the grep command on Unix.
# Ask the user to enter a regular expression and count the number of lines that matched the regular expression.

import re

try:
    file_name = input("Enter a file name: ")
    fh = open(file_name)
except:
    print("Error: File Not Found")
    quit()
else:
    expr = input("Enter a regular expression: ")

count = 0

for line in fh:
    line = line.rstrip()
    match = re.findall(expr, line)
    if len(match) < 1:
        continue
    else:
        count = count + 1

print("The file", file_name, "had", count, "lines that matched.")
