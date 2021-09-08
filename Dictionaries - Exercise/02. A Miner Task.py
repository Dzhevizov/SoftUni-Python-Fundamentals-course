collected_items = {}

item = input()

while not item == "stop":
    quantity = int(input())

    if item not in collected_items:
        collected_items[item] = quantity
    else:
        collected_items[item] += quantity

    item = input()

for item, quantity in collected_items.items():
    print(f"{item} -> {quantity}")
