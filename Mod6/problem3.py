'''Create a list of strings. Write code to create a new list that includes 
only the strings longer than three characters. Print the resulting filtered list.'''
foods = ["egg", "pizza", "tea", "apple", "rice", "ham", "banana"]
filtered_list = []
print(foods)
for words in foods:
    if len(words) > 3:
        filtered_list.append(words)
print("Food items longer than 3 characters:", filtered_list)
