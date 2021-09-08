input_list = input().split(", ")

output_list =[]
count_zeros = 0

for element in input_list:
    if element == '0':
        count_zeros += 1
    else:
        output_list.append(element)

for _ in range(count_zeros):
    output_list.append('0')

for i in range(len(output_list)):
    output_list[i] = int(output_list[i])

print(output_list)