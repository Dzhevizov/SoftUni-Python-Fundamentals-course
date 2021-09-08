dwarf_data = {}

dwarf_info = input()

while not dwarf_info == "Once upon a time":

    name, hat_color, physics = dwarf_info.split(" <:> ")

    if hat_color not in dwarf_data:
        dwarf_data[hat_color] = {}
        dwarf_data[hat_color]['name'].append(name)
        dwarf_data[hat_color]['physics'].append(int(physics))
    else:
        if name not in dwarf_data[hat_color]['name']:
            dwarf_data[hat_color]['name'].append(name)
            dwarf_data[hat_color]['physics'].append(int(physics))
        else:
            if dwarf_data[hat_color]['physics'][dwarf_data[hat_color]['name'].index(name)] < int(physics):
                dwarf_data[hat_color]['physics'][dwarf_data[hat_color]['name'].index(name)] = int(physics)

    dwarf_info = input()

for hat_color, dwarfs in sorted(dwarf_data.items(), key=lambda x: (-x[1]['physics'], -len(x[1]))):
    for name, physics in dwarf_data[hat_color].items():
        print(f"({hat_color}) {name} <-> {physics}")
