input_string = input()
output_list = []

for index, symbol in enumerate(input_string):
    if symbol.isupper():
        output_list.append(index)

print(output_list)
