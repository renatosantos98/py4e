# Exercise 1:Write a program that reads the words in words.txt and stores them as keys in a dictionary.
# It doesn't matter what the values are.
# Then you can use the in operator as a fast way to check whether a string is in the dictionary.

# Open the words.txt file.
try:
    fh = input("Enter a file name: ")
    fh = open(fh)
except:
    print("Error: File Not Found")
    quit()
else:
    # Initialise the dictionary.
    words = dict()

    # Read each line in the file and split it into words.
    for line in fh:
        line = line.split()
        for word in line:
            # Add each word in the line as a key to the dictionary with a None value assigned to it.
            words[word] = None

# Ask for input and check if that word input is a key in the dictionary.
while True:
    word_input = input("Enter a word, or type 'end input' to finish: ")
    if word_input == "end input":
        break
    else:
        print("Is the word entered in the dictionary?", word_input in words)
