to_do_notes = [0] * 10

command = input()

while not command == "End":
    importance, note = command.split("-")
    importance = int(importance)
    to_do_notes[importance - 1] = note
    command = input()

print([x for x in to_do_notes if not x == 0])
