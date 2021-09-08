import math

count_of_students = int(input())
count_of_lectures = int(input())
additional_bonus = int(input())

max_attendances = 0
max_bonus = 0

for i in range(count_of_students):

    count_of_attendances = int(input())

    total_bonus = count_of_attendances / count_of_lectures * (5 + additional_bonus)

    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_attendances = count_of_attendances

print(f'Max Bonus: {math.ceil(max_bonus)}.')
print(f'The student has attended {max_attendances} lectures.')
