neighborhood = [int(x) for x in input().split("@")]

command = input()
curr_index = 0

while not command == "Love!":

    jump = int(command.split()[1])

    curr_index += jump
    if curr_index >= len(neighborhood):
        curr_index = 0

    neighborhood[curr_index] -= 2
    if neighborhood[curr_index] == 0:
        print(f"Place {curr_index} has Valentine's day.")
    elif neighborhood[curr_index] < 0:
        print(f"Place {curr_index} already had Valentine's day.")
        neighborhood[curr_index] = 0

    command = input()

print(f"Cupid's last position was {curr_index}.")

house_counter = 0
for el in neighborhood:
    if el > 0:
        house_counter += 1

if house_counter == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {house_counter} places.")
