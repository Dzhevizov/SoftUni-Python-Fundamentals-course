targets = [int(x) for x in input().split()]

command_data = input()

while not command_data == "End":

    command, index, value = command_data.split()
    index = int(index)
    value = int(value)

    if command == "Shoot":
        if index in range(len(targets)):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)

    if command == "Add":
        if index in range(len(targets)):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    if command == "Strike":
        if index - value in range(len(targets)) and index + value in range(len(targets)):
            for _ in range(index - value, index + value + 1):
                targets.pop(index - value)
        else:
            print("Strike missed!")

    command_data = input()

targets = [str(x) for x in targets]

print("|".join(targets))
