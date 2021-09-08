contest_passwords = {}
users_data = {}

max_points = 0
best_user = ""

pass_info = input()

while not pass_info == "end of contests":

    contest, contest_pass = pass_info.split(":")
    contest_passwords[contest] = contest_pass

    pass_info = input()

users_info = input()

while not users_info == "end of submissions":

    contest, password, username, points = users_info.split("=>")

    if contest in contest_passwords and contest_passwords[contest] == password:
        if username not in users_data:
            users_data[username] = {}
            users_data[username][contest] = int(points)
        else:
            if contest not in users_data[username]:
                users_data[username][contest] = int(points)
            else:
                if users_data[username][contest] < int(points):
                    users_data[username][contest] = int(points)

    users_info = input()

for user, contests in users_data.items():
    total_points = 0

    for points in contests.values():
        total_points += points

    if max_points < total_points:
        max_points = total_points
        best_user = user

print(f"Best candidate is {best_user} with total {max_points} points.")

print("Ranking:")

for user, contests in sorted(users_data.items(), key=lambda x: x[0]):
    print(user)

    for contest, points in sorted(contests.items(), key=lambda x: -x[1]):
        print(f"#  {contest} -> {points}")
