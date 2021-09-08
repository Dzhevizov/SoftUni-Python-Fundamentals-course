num_of_people_first_employee = int(input())
num_of_people_second_employee = int(input())
num_of_people_third_employee = int(input())

total_people_count = int(input())

total_people_per_hour = num_of_people_first_employee + num_of_people_second_employee + num_of_people_third_employee

used_time = 0

while total_people_count > 0:

    used_time += 1
    if used_time % 4 == 0:
        continue

    total_people_count -= total_people_per_hour

print(f'Time needed: {used_time}h.')