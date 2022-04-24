# Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.

try:
    fh = input("Enter a file name: ")
    fh = open(fh)
except:
    print("Error: File Not Found")
    quit()
else:
    email_count = dict()
    for line in fh:
        words = line.split()
        if line.startswith("From") and len(words) > 1:
            email = words[1]
            email_count[email] = email_count.get(email, 0) + 1

print(email_count)
