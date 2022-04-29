# Exercise 1: Revise a previous program as follows: Read and parse the "From" lines and pull out the addresses from the line.
# Count the number of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary.
# Then sort the list in reverse order and print out the person who has the most commits.

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
        if line.startswith("From") and len(words) > 2:
            email = words[1]
            email_count[email] = email_count.get(email, 0) + 1

email_list = list()

for key, val in email_count.items():
    email_list.append((val, key))

email_list.sort(reverse=True)

for val, key in email_list[:1]:
    print(key, val)
