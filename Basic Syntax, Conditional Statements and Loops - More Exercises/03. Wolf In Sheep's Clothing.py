input_string = input()
input_list = input_string.split(', ')
count_sheep = 0

for i in range(len(input_list) - 1, -1, -1):
    if input_list[i] == "wolf":
        if not count_sheep:
            print("Please go away and stop eating my sheep")
        else:
            print(f"Oi! Sheep number {count_sheep}! You are about to be eaten by a wolf!")
    else:
        count_sheep += 1
