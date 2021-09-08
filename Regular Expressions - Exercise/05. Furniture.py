import re

pattern = r"^>>(?P<name>[A-Za-z]+)<<(?P<price>\d+[.]?\d*)!(?P<quantity>\d+)$"
text = input()

bought_furniture = []
total_cost = 0

while not text == "Purchase":

    matches = re.finditer(pattern, text)

    for match in matches:
        if match:
            bought_furniture.append(match.group('name'))
            total_cost += float(match.group('price')) * int(match.group('quantity'))

    text = input()

print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")
