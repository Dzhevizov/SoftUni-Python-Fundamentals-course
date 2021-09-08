collecting_items = input().split(", ")

while True:
    command_data = input().split(" - ")
    command = command_data[0]
    if command == "Craft!":
        break
    item = command_data[1]
    if command == "Collect":
        if item not in collecting_items:
            collecting_items.append(item)
    elif command == "Drop":
        if item in collecting_items:
            collecting_items.remove(item)
    elif command == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in collecting_items:
            index = collecting_items.index(old_item)
            collecting_items.insert(index + 1, new_item)
    elif command == "Renew":
        if item in collecting_items:
            collecting_items.remove(item)
            collecting_items.append(item)

print(", ".join(collecting_items))
