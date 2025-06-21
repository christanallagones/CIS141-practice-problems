# Will you fall in love with me again
Penelope
Is it you? Have my prayers been answered?
Is it really you standing there, or am I dreaming once more?
You look different, your eyes look tired
Your frame is lighter, your smile torn
Is it really you, my love?
I am not the man you fell in love with
I am not the man you once adored
I am not your kind and gentle husband
And I am not the love you knew before
Would you fall in love with me again
If you knew all I've done?
The things I cannot change
Would you love me all the same?
I know that you've been waiting, waiting for love
What kinds of things did you do?
Left a trail of red on every island
As I traded friends like objects I could use
Hurt more lives than I can count on my hands
But all of that was to bring me back to you
So tell me
Would you fall in love with me again
If you knew all I've done?
The things I can't undo
I am not the man you knew
I know that you've been waiting, waiting
If that's true, could you do me a favor?
Just a moment of labor that would bring me some peace
See that wedding bed? Could you carry it over?
Lift it high on your shoulders and take it far away from here
How could you say this?
I had built that wedding bed with my blood and sweat
Carved it into the olive tree where we first met
A symbol of our love everlasting
Do you realize what you have asked me?
The only way to move it is to cut it from its roots
Only my husband knew that
So I guess that makes him you
Penelope
I will fall in love with you over and over again
I don't care how, where, or when
No matter how long it's been, you're mine
Don't tell me you're not the same person
You're always my husband and I've been waiting, waiting
Penelope
Waiting, waiting (Penelope)
Waiting, waiting
Waiting, oh
For you
How long has it been?
Twenty years
I, I love you
'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into
it. Write a Python program that:
- Reads the file
- Requests 5 inputs from the user: 5 words the user would like to count the frequency of
- Counts how many times each word appears
- Creates a dictionary of the words and their counts
- Print the dictionary to the console
'''
with open("song_lyrics.txt", "r") as file:
    lyrics = file.read().lower()

words_to_count = []
print("Enter 5 words you'd like to count in the lyrics:")
for _ in range(5):
    word = input("Word: ").lower()
    words_to_count.append(word)

word_counts = {}
for word in words_to_count:
    count = lyrics.count(word)
    word_counts[word] = count


print("\nWord frequencies in the lyrics:")
print(word_counts)
