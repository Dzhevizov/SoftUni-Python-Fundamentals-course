my_dict = {}

product_info = input()

while not product_info == "statistics":

    product, quantity = product_info.split(": ")

    if product not in my_dict:
        my_dict[product] = int(quantity)
    else:
        my_dict[product] += int(quantity)

    product_info = input()

print("Products in stock:")
for product, quantity in my_dict.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(my_dict)}")
print(f"Total Quantity: {sum(my_dict.values())}")
