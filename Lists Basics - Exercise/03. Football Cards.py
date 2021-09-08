sequence_of_cards = input()

num_of_players = 11

teamA = []
teamB = []

sequence_of_cards_list = sequence_of_cards.split(" ")

for element in sequence_of_cards_list:
    if 'A' in element:
        teamA.append(element)
    elif 'B' in element:
        teamB.append(element)

team_A = []
team_B = []
for element in teamA:
    new_el = element.replace("A-", "")
    if int(new_el) in range(1, 12):
        team_A.append(new_el)
    if len(set(team_A)) > 4:
        break;

for element in teamB:
    new_el = element.replace("B-", "")
    if int(new_el) in range(1, 12):
        team_B.append(new_el)
    if len(set(team_B)) > 4:
        break;

print(f"Team A - {num_of_players - len(set(team_A))}; Team B - {num_of_players - len(set(team_B))}")
if num_of_players - len(set(team_A)) < 7 or num_of_players - len(set(team_B)) < 7:
    print("Game was terminated")