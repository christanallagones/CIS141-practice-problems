# Gardening_tips.txt
Water your plants early in the morning.
Use compost to enrich your soil.
Plant according to your region's climate.
'''
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to
it. Write a Python script that reads a file gardening_tips.txt and prints
out each tip one by one.
'''
with open("gardening_tips.txt", "r") as file:
    tips = file.read()
    print(tips)
