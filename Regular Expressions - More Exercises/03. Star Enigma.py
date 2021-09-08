import re

count_of_messages = int(input())

pattern = r"[star]"

attacked_planets = {}
destroyed_planets = {}

for _ in range(count_of_messages):

    encrypted_message = input()

    cypher = len(re.findall(pattern, encrypted_message.lower()))

    decrypted_message = ""
    decrypted_message1 = [chr(ord(ch) - cypher) for ch in encrypted_message]
    for ch in decrypted_message1:
        decrypted_message += ch

    pattern1 = r"[^-@!:>]*@(?P<planet_name>[A-Z][a-z]+)[^-@!:>]*:(?P<planet_population>\d+)[^-@!:>]*!(?P<attack_type>[AD])![^-@!:>]*->(?P<soldier_count>\d+)[^-@!:>]*"

    match = re.match(pattern1, decrypted_message)

    if match:
        planet_name = match.group('planet_name')
        planet_population = match.group('planet_population')
        attack_type = match.group('attack_type')
        soldier_count = match.group('soldier_count')

        if attack_type == 'A':
            attacked_planets[planet_name] = {}
            attacked_planets[planet_name] = {'planet_population': planet_population, 'soldier_count': soldier_count}
        elif attack_type == 'D':
            destroyed_planets[planet_name] = {}
            destroyed_planets[planet_name] = {'planet_population': planet_population, 'soldier_count': soldier_count}

print(f"Attacked planets: {len(attacked_planets)}")
for planet in sorted(attacked_planets):
    print(f"-> {planet}")

print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in sorted(destroyed_planets):
    print(f"-> {planet}")
