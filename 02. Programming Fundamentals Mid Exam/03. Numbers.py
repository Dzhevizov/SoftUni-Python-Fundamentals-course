integers = [int(x) for x in input().split()]

average_value = sum(integers) / len(integers)

greater_nums = [x for x in integers if x > average_value]

greater_nums.sort(reverse=True)

if not greater_nums:
    print("No")
else:
    for i in range(5):
        if i == len(greater_nums):
            break
        print(greater_nums[i], end=" ")

