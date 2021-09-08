def collect_item(collection1, object1):
    if object1 not in collection1:
        collection1.append(object1)
    return collection1


def drop_item(collection1, object1):
    if object1 in collection1:
        collection1.remove(object1)
    return collection1


def combine_item(collection1, object1, object2):
    if object1 in collection1:
        new_index = collection1.index(object1) + 1
        collection1.insert(new_index, object2)
    return collection1


def renew_item(collection1, object1):
    if object1 in collection1:
        collection1.remove(object1)
        collection1.append(object1)
    return collection1


inventory = input().split(", ")

command_data = input()

while not command_data == "Craft!":

    command_list = command_data.split(" - ")
    command = command_list[0]

    if command == "Collect":
        item = command_list[1]
        inventory = collect_item(inventory, item)
    elif command == "Drop":
        item = command_list[1]
        inventory = drop_item(inventory, item)
    elif command == "Combine Items":
        old_item, new_item = command_list[1].split(":")
        inventory = combine_item(inventory, old_item, new_item)
    elif command == "Renew":
        item = command_list[1]
        inventory = renew_item(inventory, item)

    command_data = input()

print(", ".join(inventory))
