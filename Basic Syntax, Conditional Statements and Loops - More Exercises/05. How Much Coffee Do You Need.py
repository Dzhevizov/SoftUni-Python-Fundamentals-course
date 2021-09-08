little_events = "coding,dog,cat,movie"
big_events = little_events.upper()

input_command = input()
coffee_counter = 0

while not input_command == "END":
    if input_command in little_events:
        coffee_counter += 1
    elif input_command in big_events:
        coffee_counter += 2
    input_command = input()

if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)