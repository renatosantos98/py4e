# Exercise 5: Write a program to read through the mail box data and when you find line that starts with "From", you will split the line into words using the split function.
# We are interested in who sent the message, which is the second word on the From line.
#   From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# You will parse the From line and print out the second word for each From line, then you will also count the number of From (not From:) lines and print out a count at the end.

# Try to open the file. Except if the file name is invalid.
try:
    fh = input("Enter a file name: ")
    fh = open(fh)
except:
    print("Error: File Not Found")
    quit()
else:
    # Initialise line count variable.
    count = 0
    for line in fh:
        # Only count lines starting with "From".
        if line.startswith("From"):
            # Split lines into word lists and extract the email of the sender (second word of the line).
            count = count + 1
            line_words = line.split()
            email = line_words[1]
            print(email)

print("There were", count, "lines in the file with From as the first word.")
