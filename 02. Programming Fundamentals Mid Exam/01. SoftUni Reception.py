first_employee_students_per_hour = int(input())
second_employee_students_per_hour = int(input())
third_employee_students_per_hour = int(input())

total_count_of_students = int(input())

total_students_per_hour = first_employee_students_per_hour + \
        second_employee_students_per_hour + third_employee_students_per_hour

time_needed = 0

while total_count_of_students > 0:
    time_needed += 1

    if time_needed % 4 == 0:
        continue
    else:
        total_count_of_students -= total_students_per_hour

print(f'Time needed: {time_needed}h.')
