'''Create a list of integers. Write code that counts how many numbers
are positive and how many are negative, then print both counts.'''
numbers = [12, -5, 8, -3, 27, -14, 6, 23, -21]
positive_count = 0
negative_count = 0
for num in numbers:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
print(f"Positive number count: {positive_count}")
print(f"Negative number count: {negative_count}")
