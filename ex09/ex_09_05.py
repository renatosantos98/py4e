# Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address).
# At the end of the program, print out the contents of your dictionary.

try:
    fh = input("Enter a file name: ")
    fh = open(fh)
except:
    print("Error: File Not Found")
    quit()
else:
    domain_count = dict()
    for line in fh:
        if line.startswith("From"):
            domain_start = line.find("@")
            domain_end = line.find(" ", domain_start)
            domain = line[domain_start + 1 : domain_end]
            domain_count[domain] = domain_count.get(domain, 0) + 1

print("Email Domains Found:", domain_count)
