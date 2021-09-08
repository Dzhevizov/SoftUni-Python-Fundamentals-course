cars = {}
mileage_limit = 100000
min_mileage = 10000
tank_capacity = 75

num_of_cars = int(input())

for _ in range(num_of_cars):

    car, mileage, fuel = input().split("|")
    mileage = int(mileage)
    fuel = int(fuel)

    cars[car] = {}
    cars[car] = {'mileage': mileage, 'fuel': fuel}

command = input()

while not command == "Stop":

    command = command.split(" : ")

    action = command[0]

    if action == "Drive":

        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])

        if fuel > cars[car]['fuel']:
            print("Not enough fuel to make that ride")
        else:
            cars[car]['mileage'] += distance
            cars[car]['fuel'] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

            if cars[car]['mileage'] >= mileage_limit:
                cars.pop(car)
                print(f"Time to sell the {car}!")

    elif action == "Refuel":

        car = command[1]
        fuel = int(command[2])

        empty_volume = tank_capacity - cars[car]['fuel']

        if fuel <= empty_volume:
            cars[car]['fuel'] += fuel
        else:
            fuel = tank_capacity - cars[car]['fuel']
            cars[car]['fuel'] = tank_capacity

        print(f"{car} refueled with {fuel} liters")

    elif action == "Revert":

        car = command[1]
        kilometers = int(command[2])

        cars[car]['mileage'] -= kilometers

        if cars[car]['mileage'] < min_mileage:
            cars[car]['mileage'] = min_mileage
            command = input()
            continue

        print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

for car, data in sorted(cars.items(), key= lambda x: (-x[1]['mileage'], x[0])):
    print(f"{car} -> Mileage: {data['mileage']} kms, Fuel in the tank: {data['fuel']} lt.")
