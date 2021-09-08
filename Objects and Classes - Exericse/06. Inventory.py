class Inventory:

    items = []

    def __init__(self, __capacity):
        self.__capacity = __capacity

    def add_item(self, item):
        if len(self.items) < self.__capacity:
            self.items.append(item)
        else:
            return 'not enough room in the inventory'

    def get_capacity(self):
        return self.__capacity

    def __calculate_left_capacity(self):
        return self.get_capacity() - len(self.items)

    def __repr__(self):
        return f'Items: {", ".join(self.items)}.\nCapacity left: {self.__calculate_left_capacity()}'


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
