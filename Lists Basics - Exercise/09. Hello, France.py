Collection_of_items = input().split("|")
budget = float(input())

profit = 0
income = 0

for item in Collection_of_items:
    item_info = item.split("->")
    item_type = item_info[0]
    item_price = float(item_info[1])

    if item_type == "Clothes" and item_price > 50.00:
        continue
    elif item_type == "Shoes" and item_price > 35.00:
        continue
    elif item_type == "Accessories" and item_price > 20.50:
        continue
    else:
        if item_type == "Clothes" or item_type == "Shoes" or item_type == "Accessories":
            if item_price <= budget:
                budget -= item_price
                new_price = item_price * 1.40
                profit += new_price - item_price
                income += new_price
                print(f"{new_price:.2f}", end=" ")

income += budget
print()
print(f"Profit: {profit:.2f}")
if income >= 150:
    print("Hello, France!")
else:
    print("Time to go.")