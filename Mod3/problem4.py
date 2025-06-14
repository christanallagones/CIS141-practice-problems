# Prompt user for word, first index, and last index
word = input("Enter a word:")
firstindex = int(input("Enter the first index:"))
lastindex = int(input("Enter the last index:"))
sliced = word[firstindex:lastindex]

print(sliced)
