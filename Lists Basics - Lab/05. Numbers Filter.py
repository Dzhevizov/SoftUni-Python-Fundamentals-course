num_of_integers = int(input())

full_list = []
filtered_list = []

for i in range(num_of_integers):
    curr_int = int(input())
    full_list.append(curr_int)

command = input()

if command == 'even':
    for element in full_list:
        if not element % 2:
            filtered_list.append(element)
elif command == 'odd':
    for element in full_list:
        if element % 2:
            filtered_list.append(element)
elif command == 'negative':
    for element in full_list:
        if element < 0:
            filtered_list.append(element)
elif command == 'positive':
    for element in full_list:
        if element >= 0:
            filtered_list.append(element)

print(filtered_list)