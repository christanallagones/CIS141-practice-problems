'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington
State Ferry fare based on age and whether the person has a vehicle. Assume the following rates:
* Adults (19-64): $10 without a vehicle, $20 with a vehicle.
* Seniors (65+): $5 without a vehicle, $15 with a vehicle.
* Children (0-18): Free.
'''
def ferry_fare(age, vehicle):
    if age <= 18:
        return 0 
    elif 19 <= age <= 64:
        if vehicle:
            return 20
        else:
            return 10
    elif age >= 65:
        if vehicle:
            return 15
        else:
            return 5

print(ferry_fare(25, True))
print(ferry_fare(25, False)) 
print(ferry_fare(70, True)) 
print(ferry_fare(70, False)) 
print(ferry_fare(12, False)) 
