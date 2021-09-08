num_of_strings = int(input())
word = input()

full_list = []
filtered_list = []

for i in range(num_of_strings):
    curr_string = input()
    full_list.append(curr_string)

for element in full_list:
    if word in element:
        filtered_list.append(element)

print(full_list)
print(filtered_list)
