my_dict = {}

students_info = input()

while ":" in students_info:
    name, ID, course = students_info.split(":")
    if course not in my_dict:
        my_dict[course] = []
    my_dict[course].append((name, ID))

    students_info = input()

searched_course = students_info.replace("_", " ")

for name, ID in my_dict[searched_course]:
    print(f"{name} - {ID}")

