parking_lot = {}

num_of_commands = int(input())

for _ in range(num_of_commands):

    command_info = input().split()
    command = command_info[0]

    if command == "register":
        username = command_info[1]
        license_plate_number = command_info[2]
        if username in parking_lot:
            print(f"ERROR: already registered with plate number {parking_lot[username]}")
        else:
            parking_lot[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")

    elif command == "unregister":
        username = command_info[1]
        if username not in parking_lot:
            print(f"ERROR: user {username} not found")
        else:
            parking_lot.pop(username)
            print(f"{username} unregistered successfully")

for username, license_plate_number in parking_lot.items():
    print(f"{username} => {license_plate_number}")
