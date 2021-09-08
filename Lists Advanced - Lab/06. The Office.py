employees_happiness = [int(x) for x in input().split()]
improvement_factor = int(input())

improved_happiness = [x * improvement_factor for x in employees_happiness]

average_happiness = sum(improved_happiness) / len(improved_happiness)

happy_employees_list = [x for x in improved_happiness if x >= average_happiness]

if len(happy_employees_list) >= len(improved_happiness) / 2:
    print(f'Score: {len(happy_employees_list)}/{len(improved_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(happy_employees_list)}/{len(improved_happiness)}. Employees are not happy!')
