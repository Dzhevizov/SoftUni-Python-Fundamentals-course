participants = input().split(", ")

scores = {}

race_info = input()

while not race_info == "end of race":

    name = ""
    distance = 0

    for ch in race_info:
        if ch.isalpha():
            name += ch
        elif ch.isdigit():
            distance += int(ch)

    if name in participants:
        if name not in scores:
            scores[name] = 0
        scores[name] += distance

    race_info = input()

scores = sorted(scores.items(), key=lambda x: -x[1])

print(f"1st place: {scores[0][0]}\n2nd place: {scores[1][0]}\n3rd place: {scores[2][0]}")
