products_info = input().split()
products = [products_info[i] for i in range(len(products_info)) if i % 2 == 0]
quantities = [int(products_info[i]) for i in range(len(products_info)) if not i % 2 == 0]

my_dict = dict(zip(products, quantities))
print(my_dict)

