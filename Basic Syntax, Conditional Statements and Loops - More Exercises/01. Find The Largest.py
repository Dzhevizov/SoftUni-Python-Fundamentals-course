input_digits = input()
input_digits_list = []
for i in input_digits:
    input_digits_list.append(i)
input_digits_list.sort(reverse=True)
for i in input_digits_list:
    print(i, end='')
