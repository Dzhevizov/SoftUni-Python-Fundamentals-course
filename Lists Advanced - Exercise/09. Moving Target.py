def shoot_target(list_of_integers, given_index, number):
    if given_index in range(len(list_of_integers)):
        list_of_integers[given_index] -= number
        if list_of_integers[given_index] <= 0:
            list_of_integers.pop(given_index)
    return list_of_integers


def add_target(list_of_integers, given_index, number):
    if given_index in range(len(list_of_integers)):
        list_of_integers.insert(given_index, number)
    else:
        print('Invalid placement!')
    return list_of_integers


def strike_radius_of_targets(list_of_integers, given_index, number):
    if (given_index - number) not in range(len(list_of_integers)):
        print('Strike missed!')
    elif (given_index + number) not in range(len(list_of_integers)):
        print('Strike missed!')
    else:
        for index1 in range(given_index - number, given_index + number + 1):
            list_of_integers.pop(given_index-number)
    return list_of_integers


list_of_targets = [int(x) for x in input().split()]

while True:
    command_data = input().split()
    command = command_data[0]
    if command == "End":
        break
    index = int(command_data[1])
    value = int(command_data[2])
    if command == "Shoot":
        shoot_target(list_of_targets, index, value)
    elif command == "Add":
        add_target(list_of_targets, index, value)
    elif command == "Strike":
        strike_radius_of_targets(list_of_targets, index, value)

list_of_targets = [str(x) for x in list_of_targets]
print("|".join(list_of_targets))

