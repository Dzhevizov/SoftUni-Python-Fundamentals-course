input_list = [int(x) for x in input().split(", ")]

max_value = 10

while input_list:
    output_list = [x for x in input_list if x <= max_value]
    input_list = [x for x in input_list if x not in output_list]
    print(f"Group of {max_value}'s: {output_list}")
    max_value += 10
