Cities = {}

command = input()

while not command == "Sail":

    city, population, gold = command.split("||")

    if city not in Cities:
        Cities[city] = {"population": int(population), "gold": int(gold)}
    else:
        Cities[city]["population"] += int(population)
        Cities[city]["gold"] += int(gold)

    command = input()

event = input()

while not event == "End":

    event = event.split("=>")

    action = event[0]

    if action == "Plunder":

        attacked_city = event[1]
        killed_people = int(event[2])
        plundered_gold = int(event[3])

        Cities[attacked_city]["population"] -= killed_people
        Cities[attacked_city]["gold"] -= plundered_gold

        print(f"{attacked_city} plundered! {plundered_gold} gold stolen, {killed_people} citizens killed.")

        if not Cities[attacked_city]["population"] or not Cities[attacked_city]["gold"]:

            print(f"{attacked_city} has been wiped off the map!")
            Cities.pop(attacked_city)

    if action == "Prosper":

        prospered_city = event[1]
        increased_gold = int(event[2])

        if increased_gold < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            Cities[prospered_city]["gold"] += increased_gold
            print(f"{increased_gold} gold added to the city treasury. \
{prospered_city} now has {Cities[prospered_city]['gold']} gold.")

    event = input()

if not Cities:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(Cities)} wealthy settlements to go to:")

    for city, data in sorted(Cities.items(), key= lambda x: (-x[1]["gold"], x[0])):
        print(f"{city} -> Population: {data['population']} citizens, Gold: {data['gold']} kg")
