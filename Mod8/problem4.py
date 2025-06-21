# Poll
yea, nay, yea, yea, nay, yea, nay, yea, nay, yea, nay, nay
'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated
by commas. Write a program that reads the poll.txt file
Count how many votes "yea" or "nay" received and print the results.
'''
with open("poll.txt", "r") as file:
    content = file.read()

votes = [vote.strip().lower() for vote in content.split(",")]

yea_count = votes.count("yea")
nay_count = votes.count("nay")

print(f"Yea votes: {yea_count}")
print(f"Nay votes: {nay_count}")
