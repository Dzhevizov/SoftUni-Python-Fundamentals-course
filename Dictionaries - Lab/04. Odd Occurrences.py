my_dict = {}

words = input().split()

for word in words:
    word = word.lower()
    if word not in my_dict:
        my_dict[word] = 0
    my_dict[word] += 1

for word, occurrence in my_dict.items():
    if occurrence % 2:
        print(word, end=" ")
