# Exercise 4: Add code to the above program to figure out who has the most messages in the file.
# After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Section [maximumloop]) to find who has the most messages and print how many messages the person has.

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

email_max = max(email_count, key=email_count.get)
print(email_max, email_count.get(email_max))
