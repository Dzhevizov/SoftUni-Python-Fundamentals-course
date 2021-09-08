username = input()

command = input()

while not command == "Sign up":

    command = command.split()

    action = command[0]

    if action == "Case":

        case = command[1]

        if case == "lower":
            username = username.lower()
        else:
            username = username.upper()

        print(username)

    elif action == "Reverse":

        start_index = int(command[1])
        end_index = int(command[2])

        if start_index in range(len(username)) and end_index in range(len(username)):
            substring = username[start_index:end_index + 1]
            substring = substring[::-1]

            print(substring)

    elif action == "Cut":

        substring = command[1]

        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The word {username} doesn't contain {substring}.")

    elif action == "Replace":

        char = command[1]

        username = username.replace(char, "*")
        print(username)

    elif action == "Check":

        char = command[1]

        if char in username:
            print("Valid")
        else:
            print(f"Your username must contain {char}.")

    command = input()
