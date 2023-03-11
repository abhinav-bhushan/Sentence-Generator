# Random sentences
from importlib.resources import contents
import random

# Define the name we use for the file containing the learning text
TEXTFILE = "sentences.txt"

# For the dictionary we'll use a global variable
WordPairs = {}

# This is a list of word pairs that start sentences
InitialWords = []

# Function to read the text
def readdata():
    # Use a try block to catch errors opening the file
    try:
        f = open(TEXTFILE)
        contents = f.read()
        f.close()
    except FileNotFoundError:
        return None

    return contents

# Function to build up our dictionary of word pairs
def builddictionary(Words):
    # We need to split the text into a list of single words
    wordlist = Words.split(' ')
    # Now go through the list and construct the dictionary of pairs
    for i in range(len(wordlist)-2):
        if wordlist[i][-1:] != "." and wordlist[i+1][-1:] != ".":
            key = wordlist[i] + ' ' + wordlist[i+1]
            if WordPairs.get(key) is None:
                WordPairs[key] = [wordlist[i+2]]
            else:
                WordPairs[key].append(wordlist[i+2])
        # If the word is uppercased save it and the next word as a sentence start
        if wordlist[i][0].isupper() and not wordlist[i+1][0].isupper():
            InitialWords.append([wordlist[i], wordlist[i+1]])

# Function to create a random sentence
def makesentence(FirstWord, SecondWord):
    first_word = FirstWord
    second_word = SecondWord
    sentence = first_word + " " + second_word
    num_words = 2
    # Set the maximum length to 100 words in case we don't find a word
    # ending in . or ! or ?
    while num_words < 100:
        key = first_word + " " + second_word
        # If we can't find a match stop building the sentence
        if WordPairs.get(key) is None:
            break
        # Get a next word from the dictionary and append it
        next_word = random.choice(WordPairs.get(key))
        sentence += " " + next_word
        # If the next word ends in "." this is the end of the sentence
        if next_word[-1:] == "." or next_word[-1:] == "!" or next_word[-1:] == "?":
            break
        # Finished with this pair
        first_word, second_word = second_word, next_word
    return sentence

# Main program
text = readdata()
if text is None:
    print("Cannot find the data file " + TEXTFILE)
    print("This file needs to be in the same directory as the program.")
    exit(2)

# Build the dictionary of word pairs
builddictionary(text)
print(WordPairs)
# Prompt the user for two words
print("Enter two words to start the sentence. Press enter to let the program choose.")
two_words = input("Type the two words separated by a space e.g. the dog: ")

# If the user just pressed enter choose a pair initial words at random
if two_words == "":
    words = random.choice(InitialWords)
# Else use the two words the user entered
else:
    words = two_words.split(" ")
    if len(words) != 2:
        print("You need to type two words separated by a space.")
        exit(2)

print("Using the words: " + words[0] + " " + words[1])
s = makesentence(words[0], words[1])
print(s)
