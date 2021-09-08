import math
list_of_numbers = input().split(" ")

half_len = math.floor(len(list_of_numbers) / 2)

left_distance = list_of_numbers[:half_len]
right_distance = (list_of_numbers[half_len + 1:])

left_sum = 0
right_sum = 0

for i in range(len(left_distance)):
    left_sum += int(left_distance[i])
    if int(left_distance[i]) == 0:
        left_sum *= 0.8

for i in range(-1, -len(right_distance) - 1, -1):
    right_sum += int(right_distance[i])
    if int(right_distance[i]) == 0:
        right_sum *= 0.8

if left_sum <= right_sum:
    print(f"The winner is left with total time: {left_sum:.1f}")
else:
    print(f"The winner is right with total time: {right_sum:.1f}")


