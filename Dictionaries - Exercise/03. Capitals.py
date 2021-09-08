countries = [x for x in input().split(", ")]
capitals = [x for x in input().split(", ")]
my_dict = dict(zip(countries, capitals))

for country, capital in my_dict.items():
    print(f"{country} -> {capital}")
