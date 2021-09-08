numbers_list = [int(x) for x in input().split(", ")]

indexes_list = []

for i in range(len(numbers_list)):
    if numbers_list[i] % 2 == 0:
        indexes_list.append(i)

print(indexes_list)
