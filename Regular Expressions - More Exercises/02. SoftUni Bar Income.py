import re

pattern = r"%(?P<name>[A-Z][a-z]+)%[^|$%.]*<(?P<product>\w+)>[^|$%.]*\|(?P<count>\d+)\|[^|$%.\d]*(?P<price>[0-9]+\.?\d+)\$"
text = input()

total = 0

while not text == "end of shift":

    match = re.match(pattern, text)

    if match:
        name = match.group('name')
        product = match.group('product')
        count = int(match.group('count'))
        price = float(match.group('price'))

        total += count * price

        print(f"{name}: {product} - {count * price:.2f}")

    text = input()

print(f"Total income: {total:.2f}")
