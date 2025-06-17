'''
A store charges $5 for shipping on any order under $50. If the order amount is $50 or more, shipping is free. 
Ask the user for the order total and print the total cost, including shipping.
'''
shipping = 5
order = int(input("Enter the order amount:"))
if order < 50:
    total_order = order + shipping
    print(f"${total_order}")
else:
    print(f"${order}")
