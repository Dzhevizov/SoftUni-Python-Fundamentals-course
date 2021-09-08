battlefield = {}

command = input()

while not command == "Results":

    command = command.split(":")

    action = command[0]

    if action == "Add":

        person = command[1]
        health = int(command[2])
        energy = int(command[3])

        if person not in battlefield:
            battlefield[person] = {}
            battlefield[person] = {'health': health, 'energy': energy}
        else:
            battlefield[person]['health'] += health

    elif action == "Attack":

        attacker = command[1]
        defender = command[2]
        damage = int(command[3])

        if attacker in battlefield and defender in battlefield:
            battlefield[attacker]['energy'] -= 1
            battlefield[defender]['health'] -= damage

            if battlefield[defender]['health'] <= 0:
                battlefield.pop(defender)
                print(f"{defender} was disqualified!")

            if battlefield[attacker]['energy'] <= 0:
                battlefield.pop(attacker)
                print(f"{attacker} was disqualified!")

    elif action == "Delete":

        person = command[1]

        if person == "All":
            battlefield = {}
        else:
            if person in battlefield:
                battlefield.pop(person)

    command = input()

print(f"People count: {len(battlefield)}")

for person, data in sorted(battlefield.items(), key= lambda x: (-x[1]['health'], x[0])):
    print(f"{person} - {data['health']} - {data['energy']}")
