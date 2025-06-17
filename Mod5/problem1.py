# Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n. Print the final sum.
n = int(input("Enter a positive integer:"))
total = 0
integer = 1
while integer <= n:
    total += integer
    integer += 1
print(f"The final sum from 1 to {n} is: {total}")
