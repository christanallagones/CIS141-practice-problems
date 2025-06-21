'''
#2. Write a Python program that allows users to log their hiking trips. The program
should:
- Use a while loop to repeatedly ask for a hike name and distance in miles
- Save each entry to hiking_log.txt (each hike on a new line)
- When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''
with open("hiking_log.txt", "a") as log_file:
    while True:
        hike_name = input("Enter the name of the hike (or 0 to quit): ")
        if hike_name == "0":
            break

        distance = input("Enter the distance in miles: ")
        if distance == "0":
            break

        log_file.write(f"{hike_name} - {distance} miles\n")

print("\n📖 Your Hiking Log:")
with open("hiking_log.txt", "r") as log_file:
    for line in log_file:
        print(f"{line}, \n")
