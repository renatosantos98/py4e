# Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done.
# To do this look for lines that start with "From", then look for the third word and keep a running count of each of the days of the week.
# At the end of the program print out the contents of your dictionary (order does not matter).

try:
    fh = input("Enter a file name: ")
    fh = open(fh)
except:
    print("Error: File Not Found")
    quit()
else:
    # Initialise the dictionary.
    week_days = dict()
    for line in fh:
        words = line.split()
        # Only count lines starting with "From" and that contain at least 3 words.
        if line.startswith("From") and len(words) > 2:
            day = words[2]
            week_days[day] = week_days.get(day, 0) + 1

print(week_days)
