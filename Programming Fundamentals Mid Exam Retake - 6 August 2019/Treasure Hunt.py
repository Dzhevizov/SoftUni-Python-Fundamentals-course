treasure_chest = input().split("|")

command_data = input()

while not command_data == "Yohoho!":

    command_list = command_data.split()

    command = command_list[0]

    if command == "Loot":
        for i in range(1, len(command_list)):
            if command_list[i] not in treasure_chest:
                treasure_chest.insert(0, command_list[i])

    elif command == "Drop":
        index = int(command_list[1])
        if index in range(len(treasure_chest)):
            temp = treasure_chest[index]
            treasure_chest.pop(index)
            treasure_chest.append(temp)

    elif command == "Steal":
        count = int(command_list[1])
        stolen_items = []
        for i in range(count):
            stolen_items.append(treasure_chest[-1])
            treasure_chest.pop(-1)
            if not treasure_chest:
                break
        for i in range(-1, -len(stolen_items) -1, -1):
            if i == -len(stolen_items):
                print(stolen_items[i])
            else:
                print(stolen_items[i], end=", ")

    command_data = input()

if not treasure_chest:
    print("Failed treasure hunt.")
else:
    length_sum = 0
    for i in range(len(treasure_chest)):
        length_sum += len(treasure_chest[i])

    average_gain = length_sum / len(treasure_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
