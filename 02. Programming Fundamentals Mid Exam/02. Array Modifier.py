numbers = [int(x) for x in input().split()]

command_data = input()

while not command_data == "end":

    command_list = command_data.split()

    command = command_list[0]

    if command == "swap":
        index1 = int(command_list[1])
        index2 = int(command_list[2])

        numbers[index1], numbers[index2] = numbers[index2], numbers[index1]

    elif command == "multiply":
        index1 = int(command_list[1])
        index2 = int(command_list[2])

        numbers[index1] *= numbers[index2]

    elif command == "decrease":
        for i in range(len(numbers)):
            numbers[i] -= 1

    command_data = input()

numbers = [str(x) for x in numbers]

print(", ".join(numbers))
