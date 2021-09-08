grades = {}

num_of_grades = int(input())

for _ in range(num_of_grades):

    student = input()
    grade = float(input())

    if student not in grades:
        grades[student] = []

    grades[student].append(grade)

av_grades = {}

for key, value in grades.items():
    av_grade = sum(value) / len(value)
    av_grades[key] = av_grade

filtered_students = {st: gr for (st, gr) in av_grades.items() if gr >= 4.50}

for st, gr in sorted(filtered_students.items(), key=lambda x: -x[1]):
    print(f"{st} -> {gr:.2f}")
