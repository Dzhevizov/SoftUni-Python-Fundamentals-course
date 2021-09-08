class Catalogue:

    products = []

    def __init__(self, name):
        self.name = name

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        return [x for x in self.products if x.startswith(first_letter)]

    def make_list_of_sorted_products(self):
        return "\n".join(sorted(self.products))

    def __repr__(self):
        return f'Items in the {self.name} catalogue: \n{self.make_list_of_sorted_products()}'


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)



