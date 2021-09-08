lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
count_shield_breaks = 0

for i in range(1, lost_fights_count + 1):
    if not i % 2:
        expenses += helmet_price
    if not i % 3:
        expenses += sword_price
        if not i % 2:
            expenses += shield_price
            count_shield_breaks += 1
    if count_shield_breaks == 2:
        expenses += armor_price
        count_shield_breaks = 0

print(f"Gladiator expenses: {expenses:.2f} aureus")