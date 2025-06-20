'''
Write a function called count_vowels(input) that takes a string
and returns the number of vowels (a, e, i, o, u) in it.
'''
def count_vowels(input):
    vowels = "aeiou"
    count = 0
    for char in input:
        if char in vowels:
            count += 1
    return count

user = input("Enter a string:")
vowel_count = count_vowels(user)
print(f"The number of vowels is: {vowel_count}")
