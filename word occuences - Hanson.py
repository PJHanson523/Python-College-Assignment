'''finds how many of a requested word occurs in a given sentence'''

string = input("Sentence: ")
word = input("Word to look for in sentence: ")
count = 0

# Sanatize input
string = string.strip()
string = string.lower()
word = word.strip()
word = word.lower()

# Make a list from inputed sentence
senlist = string.split()

# Find how many instances of the inputed word there is in the list
fcount = senlist.count(word)

print("There are", fcount, "occurrences of", word, "in the sentence.")
