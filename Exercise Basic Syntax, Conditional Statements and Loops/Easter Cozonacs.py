budget = float(input())
flour_price = float(input())

eggs_price = 0.75 * flour_price
milk_price = 1.25 * flour_price / 4

cozonac_price = eggs_price + flour_price + milk_price
cozonac_count = 0
colored_eggs = 0
cozonac_cost = 0

while (cozonac_cost + cozonac_price) < budget:
    cozonac_count += 1
    cozonac_cost = cozonac_count * cozonac_price
    colored_eggs += 3
    if cozonac_count % 3 == 0:
        colored_eggs -= cozonac_count - 2

print(f'You made {cozonac_count} cozonacs! Now you have {colored_eggs} eggs and {budget-cozonac_cost:.2f}BGN left.')
