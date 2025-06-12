# Prompt user for three side lengths of a triangle
a = int(input("Enter your first side length of a triangle"))
b = int(input("Enter your second side length of a triangle"))
c = int(input("Enter your third side length of a triangle"))

# Perform operations
from math import sqrt
s = 0.5 * (a + b + c)
A = sqrt(s * (s - a) * (s - b) * (s - c))

# Display results
print(f"Results:")
print(f"{a} + {b} + {c} * {1/2} = {s}")
print(f"sqrt ({s} * ({s} - {a}) * ({s} - {b}) * ({s} - {c}) = {A}")
print(f"The area of the triangle is {A}.")


