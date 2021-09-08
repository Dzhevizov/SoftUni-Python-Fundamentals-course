order = {}

product_info = input()

while not product_info == "buy":
    product_info_list = product_info.split()
    product_name = product_info_list[0]
    product_price = float(product_info_list[1])
    product_quantity = int(product_info_list[2])

    if product_name not in order:
        order[product_name] = [product_price, product_quantity]
    else:
        if not order[product_name][0] == product_price:
            order[product_name][0] = product_price
        order[product_name][1] += product_quantity

    product_info = input()

for product in order:
    print(f"{product} -> {order[product][0]*order[product][1]:.2f}")
