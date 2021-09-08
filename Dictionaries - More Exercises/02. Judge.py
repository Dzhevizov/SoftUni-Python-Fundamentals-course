contest_dict = {}
individual_dict = {}

results_info = input()

while not results_info == "no more time":

    username, contest, points = results_info.split(" -> ")

    if contest not in contest_dict:
        contest_dict[contest] = {}
        contest_dict[contest][username] = int(points)
    else:
        if username not in contest_dict[contest]:
            contest_dict[contest][username] = int(points)
        else:
            if contest_dict[contest][username] < int(points):
                contest_dict[contest][username] = int(points)

    if username not in individual_dict:
        individual_dict[username] = {}
        individual_dict[username][contest] = int(points)
    else:
        if contest not in individual_dict[username]:
            individual_dict[username][contest] = int(points)
        else:
            if individual_dict[username][contest] < int(points):
                individual_dict[username][contest] = int(points)

    results_info = input()

for contest, users in contest_dict.items():
    print(f"{contest}: {len(users)} participants")

    position = 1
    for user, points in sorted(users.items(), key=lambda x: (-x[1], x[0])):
        print(f"{position}. {user} <::> {points}")
        position += 1

individual_points = {}

for user, contests in individual_dict.items():
    total_points = 0
    for points in contests.values():
        total_points += points
    individual_points[user] = total_points

print("Individual standings:")

ind_position = 1
for user, points in sorted(individual_points.items(), key=lambda x: (-x[1], x[0])):
    print(f"{ind_position}. {user} -> {points}")
    ind_position += 1
