input_list = input().split(".")
input_list = [int(x) for x in input_list]
input_list[2] = input_list[2] + 1

if input_list[2] > 9:
    input_list[2] = 0
    input_list[1] += 1
    if input_list[1] > 9:
        input_list[1] = 0
        input_list[0] += 1
input_list = [str(x) for x in input_list]

output = ".".join(input_list)
print(output)
