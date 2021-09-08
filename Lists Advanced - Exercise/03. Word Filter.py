input_list = input().split()
filtered_list = [x for x in input_list if len(x) % 2 == 0]
for x in filtered_list:
    print(x)