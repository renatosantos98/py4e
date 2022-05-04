# Exercise 2: This program counts the distribution of the hour of the day for each of the messages.
# You can pull the hour from the "From" line by finding the time string and then splitting that string into parts using the colon character.
# Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour.

try:
    fh = input("Enter a file name: ")
    fh = open(fh)
except:
    print("Error: File Not Found")
    quit()
else:
    hour_count = dict()
    for line in fh:
        words = line.split()
        if line.startswith("From") and len(words) > 2:
            time = words[5].split(":")
            hour = time[0]
            hour_count[hour] = hour_count.get(hour, 0) + 1

for key, val in sorted(hour_count.items()):
    print(key, val)
