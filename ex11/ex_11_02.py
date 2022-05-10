# Exercise 2: Write a program to look for lines of the form
# "New Revision: 39772"
# and extract the number from each of the lines using a regular expression and the findall() method.
# Compute the average of the numbers and print out the average.

import re

try:
    file_name = input("Enter a file name: ")
    fh = open(file_name)
except:
    print("Error: File Not Found")
    quit()
else:
    total = 0
    count = 0

for line in fh:
    line = line.rstrip()
    number = re.findall("New Revision: ([0-9]+)", line)
    for n in number:
        n = float(n)
        total = total + n
        count = count + 1

avg = total / count

print(avg)
