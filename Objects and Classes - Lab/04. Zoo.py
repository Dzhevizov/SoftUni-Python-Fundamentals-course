class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name

        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        self.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f'Mammals in {self.name}: {", ".join(self.mammals)} \nTotal animals: {self.__animals}'
        elif species == "fish":
            return f'Fishes in {self.name}: {", ".join(self.fishes)} \nTotal animals: {self.__animals}'
        elif species == "bird":
            return f'Birds in {self.name}: {", ".join(self.birds)} \nTotal animals: {self.__animals}'


zoo_name = input()
my_zoo = Zoo(zoo_name)

number = int(input())

for num in range(number):
    species, name = input().split()
    my_zoo.add_animal(species, name)

searched_species = input()
print(my_zoo.get_info(searched_species))
