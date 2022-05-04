# Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency.
# Your program should convert all the input to lower case and only count the letters a-z.
# Your program should not count spaces, digits, punctuation, or anything other than the letters a-z.

try:
    fh = input("Enter a file name: ")
    fh = open(fh)
except:
    print("Error: File Not Found")
    quit()
else:
    words = fh.read().lower()

letters = list()
letter_count = dict()

for character in words:
    if character.isalpha() == True:
        letters.append(character)

for letter in letters:
    letter_count[letter] = letter_count.get(letter, 0) + 1

letters.clear()

for key, val in letter_count.items():
    letters.append((val, key))

letters.sort(reverse=True)

for val, key in letters:
    print(key, val)
