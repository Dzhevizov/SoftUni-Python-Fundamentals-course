users_points = {}
language_submissions = {}

submission_info = input()

while not submission_info == "exam finished":
    if "banned" not in submission_info:
        username, language, points = submission_info.split("-")

        if username not in users_points:
            users_points[username] = int(points)
        else:
            if users_points[username] < int(points):
                users_points[username] = int(points)

        if language not in language_submissions:
            language_submissions[language] = 1
        else:
            language_submissions[language] += 1

    else:
        username = submission_info.split("-")[0]
        users_points.pop(username)

    submission_info = input()

print("Results:")

for username, points in sorted(users_points.items(), key=lambda x: (-x[1], x[0])):
    print(f"{username} | {points}")

print("Submissions:")

for language, submissions in sorted(language_submissions.items(), key=lambda x: (-x[1], x[0])):
    print(f"{language} - {submissions}")
