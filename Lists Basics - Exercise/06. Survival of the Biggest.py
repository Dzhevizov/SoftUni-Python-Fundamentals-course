import sys
input_numbers_list = input().split(" ")
numbers_to_remove = int(input())

for i in range(numbers_to_remove):
    min_num = sys.maxsize
    for element in input_numbers_list:
        element = int(element)
        if element < min_num:
            min_num = element
    input_numbers_list.remove(str(min_num))

for element in input_numbers_list:
    if element == input_numbers_list[-1]:
        print(element)
    else:
        print(element, end=", ")
