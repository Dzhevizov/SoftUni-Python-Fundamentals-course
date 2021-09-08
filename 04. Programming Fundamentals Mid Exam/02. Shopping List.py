groceries = input().split("!")

command_data = input()

while not command_data == "Go Shopping!":

    command_list = command_data.split()

    command = command_list[0]

    if command == "Urgent":
        item = command_list[1]
        if item not in groceries:
            groceries.insert(0, item)

    elif command == "Unnecessary":
        item = command_list[1]
        if item in groceries:
            groceries.remove(item)

    elif command == "Correct":
        old_item = command_list[1]
        new_item = command_list[2]
        if old_item in groceries:
            groceries.insert(groceries.index(old_item), new_item)
            groceries.remove(old_item)

    elif command == "Rearrange":
        item = command_list[1]
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)

    command_data = input()

print(", ".join(groceries))
