def order_calculator(item, num):
    price = 0
    if item == "coffee":
        price = 1.50
    elif item == "water":
        price = 1.00
    elif item == "coke":
        price = 1.40
    elif item == "snacks":
        price = 2.00
    return price * num


product = input()
quantity = int(input())
print(f'{order_calculator(product, quantity):.2f}')
