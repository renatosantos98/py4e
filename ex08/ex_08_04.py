# Exercise 4: Write a program to open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split function.
# For each word, check to see if the word is already in a list. If the word is not in the list, add it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.

# Initialise word list.
word_list = []

# Try to open the file. Except if the file name is invalid.
try:
    fh = input("Enter a file name: ")
    fh = open(fh)
except:
    print("Error: File Not Found")
    quit()
else:
    for line in fh:
        # Split each line into a list of words.
        line_words = line.split()
        # print("Debug - Words in Line: ", line_words)
        # Check if line is empty. If so, skip it.
        if len(line_words) == 0:
            continue
        # Check if each of the words is on the word list. If the word is not on the list, append that word to the list.
        for word in line_words:
            # print("Debug - Word: ", word)
            if word not in word_list:
                word_list.append(word)

# print("Debug - Word List: ", word_list)
# Sort the list into alphabetical order and print.
word_list.sort()
print(word_list)
