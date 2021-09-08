numbers = [int(x) for x in input().split()]

commands_data = input()

while not commands_data == "Finish":

    command_list = commands_data.split()
    command = command_list[0]

    if command == "Add":
        value = int(command_list[1])
        numbers.append(value)

    elif command == "Remove":
        value = int(command_list[1])
        if value in numbers:
            numbers.remove(value)

    elif command == "Replace":
        value = int(command_list[1])
        replacement = int(command_list[2])
        if value in numbers:
            index = numbers.index(value)
            if replacement:
                numbers.insert(index, replacement)
                numbers.remove(value)

    elif command == "Collapse":
        value = int(command_list[1])
        numbers = [x for x in numbers if x >= value]

    commands_data = input()

print(*numbers)
