event_list = input().split("|")

energy = 100
coins = 100

is_closed = False

for event in event_list:
    event_info = event.split("-")
    event_name = event_info[0]
    event_number = int(event_info[1])

    if event_name == "rest":
        if energy + event_number > 100:
            event_number = 100 - energy
            energy = 100
        else:
            energy += event_number
        print(f"You gained {event_number} energy.")
        print(f"Current energy: {energy}.")
    elif event_name == "order":
        if energy >= 30:
            energy -= 30
            coins += event_number
            print(f"You earned {event_number} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if event_number < coins:
            coins -= event_number
            print(f"You bought {event_name}.")
        else:
            print(f"Closed! Cannot afford {event_name}.")
            is_closed = True
            break

if not is_closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")