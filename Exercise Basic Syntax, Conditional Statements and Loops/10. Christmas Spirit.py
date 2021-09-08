allowed_quantity = int(input())
days_left = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_lights_price = 15

christmas_spirit = 0
total_costs = 0

for curr_day in range(1,days_left + 1):
    if curr_day % 11 == 0:
        allowed_quantity += 2
    if curr_day % 2 == 0:
        total_costs += allowed_quantity * ornament_set_price
        christmas_spirit += 5
    if curr_day % 3 == 0:
        total_costs += allowed_quantity * tree_skirt_price + allowed_quantity * tree_garlands_price
        christmas_spirit += 13
    if curr_day % 5 == 0:
        total_costs += allowed_quantity * tree_lights_price
        christmas_spirit += 17
        if curr_day % 3 == 0:
            christmas_spirit += 30
    if curr_day % 10 == 0:
        total_costs += tree_skirt_price + tree_garlands_price + tree_lights_price
        christmas_spirit -= 20
        if curr_day == days_left:
            christmas_spirit -= 30

print(f"Total cost: {total_costs}")
print(f"Total spirit: {christmas_spirit}")

