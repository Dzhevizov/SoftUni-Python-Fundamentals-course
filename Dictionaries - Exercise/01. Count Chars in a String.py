input_string = input()
my_dict = {}

for char in input_string:
    if char == ' ':
        continue
    else:
        my_dict[char] = input_string.count(char)

for key, value in my_dict.items():
    print(f'{key} -> {value}')
