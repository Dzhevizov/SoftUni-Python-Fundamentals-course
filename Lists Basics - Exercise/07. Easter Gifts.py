list_of_gifts = input().split(" ")

command = input()

while not command == "No Money":
    if "OutOfStock" in command:
        command_list = command.split(" ")
        for i in range(len(list_of_gifts)):
            if command_list[1] == list_of_gifts[i]:
                list_of_gifts[i] = "None"
    elif "Required" in command:
        command_list = command.split(" ")
        command_list[2] = int(command_list[2])
        if command_list[2] in range(len(list_of_gifts)):
            list_of_gifts[command_list[2]] = command_list[1]
    elif "JustInCase" in command:
        command_list = command.split(" ")
        list_of_gifts[-1] = command_list[1]

    command = input()

for element in list_of_gifts:
    if not element == "None":
        print(element, end=" ")
