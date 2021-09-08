input_list = input().split(" ")

input_list.sort(reverse=True)

for element in input_list:
    print(element, end="")