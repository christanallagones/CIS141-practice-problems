# Create a list of integers (you get to pick!). 
# Write code to iterate through the list and calculate the sum of all even numbers. 
# Print the resulting sum.
integers = [2, 6, 15, 9, 26, 41, 37, 19]
sum_even = 0
for i in integers:
    if i % 2 == 0:
        print(f"{sum_even} + {i}")
        sum_even += i
print(f"The sum of all even numbers is: {sum_even}")
