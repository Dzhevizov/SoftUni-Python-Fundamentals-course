raw_activation_key = input()

instructions = input()

while not instructions == "Generate":

    instructions = instructions.split(">>>")

    if instructions[0] == "Contains":

        substring = instructions[1]

        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif instructions[0] == "Flip":

        up_low = instructions[1]
        start_index = int(instructions[2])
        end_index = int(instructions[3])

        if up_low == "Lower":

            raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[start_index:end_index].lower() +\
                                 raw_activation_key[end_index:]

            print(raw_activation_key)

        elif up_low == "Upper":

            raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[start_index:end_index].upper() +\
                                 raw_activation_key[end_index:]

            print(raw_activation_key)

    elif instructions[0] == "Slice":

        start_index = int(instructions[1])
        end_index = int(instructions[2])

        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]

        print(raw_activation_key)

    instructions = input()

print(f"Your activation key is: {raw_activation_key}")