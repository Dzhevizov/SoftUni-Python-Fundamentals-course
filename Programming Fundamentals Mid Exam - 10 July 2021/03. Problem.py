deck = input().split(":")
new_deck = []

command_data = input()

while not command_data == "Ready":

    command_list = command_data.split()
    command = command_list[0]

    if command == "Add":
        card_name = command_list[1]
        if card_name in deck:
            new_deck.append(card_name)
        else:
            print("Card not found.")

    elif command == "Insert":
        card_name = command_list[1]
        index = int(command_list[2])
        if card_name not in deck or index not in range(len(new_deck)):
            print("Error!")
        else:
            new_deck.insert(index, card_name)

    elif command == "Remove":
        card_name = command_list[1]
        if card_name in new_deck:
            new_deck.remove(card_name)
        else:
            print("Card not found.")

    elif command == "Swap":
        card_name1 = command_list[1]
        card_name2 = command_list[2]
        is_found = False
        for i in range(len(new_deck)):
            for j in range(len(new_deck)):
                if new_deck[i] == card_name1 and new_deck[j] == card_name2:
                    new_deck[i], new_deck[j] = new_deck[j], new_deck[i]
                    is_found = True
                    break
            if is_found:
                break

    elif command == "Shuffle":
        new_deck = new_deck[::-1]

    command_data = input()

print(*new_deck)