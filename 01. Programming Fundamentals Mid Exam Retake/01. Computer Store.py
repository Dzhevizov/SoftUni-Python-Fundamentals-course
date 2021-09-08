prices = input()
taxes = 0.2
special_discount = 0.1
total_neto_price = 0
total_taxes = 0
total_price = 0

while not (prices == "special" or prices == "regular"):
    prices = float(prices)

    if prices <= 0:
        print("Invalid price!")
    else:
        total_neto_price += prices
        total_taxes += taxes * prices

    prices = input()

total_price = total_neto_price + total_taxes

if prices == "special":
    total_price -= total_price * special_discount

if not total_price:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\n\
Price without taxes: {total_neto_price:.2f}$\n\
Taxes: {total_taxes:.2f}$\n\
-----------\n\
Total price: {total_price:.2f}$")
