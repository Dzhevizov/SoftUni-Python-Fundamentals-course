input_string = input()

output_list = input_string.split(" ")
for i in range(len(output_list)):
    output_list[i] = int(output_list[i]) * (-1)

print(output_list)
