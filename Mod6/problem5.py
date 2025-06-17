'''Create a list of integers. Use a loop to build a new list 
where each element is the square of the corresponding element in the original list. Print the new list.'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared = []
for num in numbers:
    squared.append(num ** 2)
print(numbers)
print(f"Each number squared: {squared}")
