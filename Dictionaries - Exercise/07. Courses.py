courses = {}

course_info = input()

while not course_info == "end":

    course_name, student_name = course_info.split(" : ")

    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

    course_info = input()

for course_name, students_list in sorted(courses.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"{course_name}: {len(students_list)}")
    for student in sorted(students_list):
        print(f"-- {student}")
