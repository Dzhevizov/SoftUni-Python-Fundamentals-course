players_data = {}

command = input()

while not command == "Season end":

    if "->" in command:
        player, position, skill = command.split(" -> ")

        if player not in players_data:
            players_data[player] = {}
            players_data[player][position] = int(skill)
        else:
            if position not in players_data[player]:
                players_data[player][position] = int(skill)
            else:
                if players_data[player][position] < int(skill):
                    players_data[player][position] = int(skill)

    elif "vs" in command:
        player1, player2 = command.split(" vs ")

        if player1 in players_data and player2 in players_data:

            is_found = False

            for position in players_data[player1]:
                if position in players_data[player2]:
                    is_found = True
                    break

            if is_found:

                total_skills_pl1 = 0
                total_skills_pl2 = 0

                for skill in players_data[player1].values():
                    total_skills_pl1 += skill
                for skill in players_data[player2].values():
                    total_skills_pl2 += skill

                if total_skills_pl1 < total_skills_pl2:
                    players_data.pop(player1)
                elif total_skills_pl2 < total_skills_pl1:
                    players_data.pop(player2)

    command = input()

players_skills = {}

for player, positions in players_data.items():
    total_skills = 0
    for skill in players_data[player].values():
        total_skills += skill
    players_skills[player] = total_skills

for player, total_skills in sorted(players_skills.items(), key=lambda x: (-x[1], x[0])):
    print(f"{player}: {total_skills} skill")

    for position, skill in sorted(players_data[player].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {position} <::> {skill}")
