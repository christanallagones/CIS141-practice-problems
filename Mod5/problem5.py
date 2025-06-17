# Write a program that continuously asks the user to input a number. 
# If the user enters 0, immediately stop asking for more numbers. Otherwise, print the number they entered.
number = int(input("Enter a number (0 to stop):"))
while True:
    if number == 0:
        print("Exiting...")
        break
        
    else:
        print(f"You entered: {number}")
        number = int(input("Enter a number (0 to stop):"))
