'''
Prompt the user for their bank balance. 
Evaluate whether the balance is less than $100. 
Print True if the user’s balance is below $100; print False, otherwise.
'''
balance = int(input("Enter your bank balance"))
if balance < 100:
    print("True")
else:
    print("False")
