class Party:
    def __init__(self):
        self.people = []

    def add_people(self, guest):
        self.people.append(guest)


my_party = Party()
name = input()

while not name == "End":
    my_party.add_people(name)
    name = input()

print(f'Going: {", ".join(my_party.people)}')
print(f'Total: {len(my_party.people)}')

