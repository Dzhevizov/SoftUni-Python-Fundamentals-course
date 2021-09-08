products_info = input().split()
products = [products_info[i] for i in range(len(products_info)) if i % 2 == 0]
quantities = [int(products_info[i]) for i in range(len(products_info)) if not i % 2 == 0]

my_dict = dict(zip(products, quantities))

searched_products = input().split()

for product in searched_products:
    if product in my_dict:
        print(f"We have {my_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
