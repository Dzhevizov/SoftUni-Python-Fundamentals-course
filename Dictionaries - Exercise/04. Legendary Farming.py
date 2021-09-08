key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}

is_found = False

while True:
    farmed_elements = input().split()
    materials_names = [farmed_elements[i].lower() for i in range(len(farmed_elements)) if not i % 2 == 0]
    materials_quantity = [int(farmed_elements[i]) for i in range(len(farmed_elements)) if i % 2 == 0]

    for i in range(len(materials_names)):
        if materials_names[i] in key_materials:
            key_materials[materials_names[i]] += materials_quantity[i]
        else:
            if materials_names[i] in junk:
                junk[materials_names[i]] += materials_quantity[i]
            else:
                junk[materials_names[i]] = materials_quantity[i]

        for key, value in key_materials.items():
            if key_materials["shards"] >= 250:
                print("Shadowmourne obtained!")
                key_materials["shards"] -= 250
                is_found = True
                break
            elif key_materials["fragments"] >= 250:
                print("Valanyr obtained!")
                key_materials["fragments"] -= 250
                is_found = True
                break
            elif key_materials["motes"] >= 250:
                print("Dragonwrath obtained!")
                key_materials["motes"] -= 250
                is_found = True
                break

        if is_found:
            break

    if is_found:
        break

for key, value in sorted(key_materials.items(), key=lambda x: (-x[1], x[0])):
    print(f"{key}: {value}")

for key, value in sorted(junk.items(), key=lambda x: x[0]):
    print(f"{key}: {value}")
