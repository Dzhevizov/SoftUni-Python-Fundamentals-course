number_list = input().split(" ")
input_string = input()

sum_numbers = []
element_sum = 0

char_list = []

for element in number_list:
    for digit in element:
        element_sum += int(digit)
    sum_numbers.append(element_sum)
    element_sum = 0

for element in input_string:
    char_list.append(element)

for i in sum_numbers:
    while i >= len(char_list):
        i -= len(char_list)
    print(char_list[i], end='')
    char_list.remove(char_list[i])