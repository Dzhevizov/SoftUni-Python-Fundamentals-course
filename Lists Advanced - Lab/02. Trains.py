num_of_wagons = int(input())
train = [0] * num_of_wagons

command = input()

while not command == "End":
    command = command.split()
    if command[0] == "add":
        people = int(command[1])
        train[-1] += people
    elif command[0] == "insert":
        index, people = int(command[1]), int(command[2])
        train[index] += people
    elif command[0] == "leave":
        index, people = int(command[1]), int(command[2])
        train[index] -= people

    command = input()

print(train)
