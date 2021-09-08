def decrease_hearts(input_list, input_index):
    input_list[input_index] -= 2
    if input_list[input_index] == 0:
        print(f"Place {input_index} has Valentine's day.")
    elif input_list[input_index] < 0:
        print(f"Place {input_index} already had Valentine's day.")
    return input_list


def count_houses(input_list):
    house_count = 0
    for house in input_list:
        if house > 0:
            house_count += 1
    return house_count


needed_hearts_list = [int(x) for x in input().split("@")]
curr_index = 0

while True:
    command_data = input().split()
    command = command_data[0]
    if command == "Love!":
        break
    jump = int(command_data[1])
    index = curr_index + jump
    if index not in range(len(needed_hearts_list)):
        index = 0
    decrease_hearts(needed_hearts_list, index)
    curr_index = index

print(f"Cupid's last position was {curr_index}.")
houses_counter = count_houses(needed_hearts_list)
if houses_counter == 0:
    print('Mission was successful.')
else:
    print(f'Cupid has failed {houses_counter} places.')
