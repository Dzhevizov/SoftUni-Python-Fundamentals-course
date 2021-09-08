import re

pattern = r"(^|(?<=\s))\+359(?P<delimiter>\s|-)2(?P=delimiter)[0-9]{3}(?P=delimiter)[0-9]{4}\b"
text = input()

matches = re.finditer(pattern, text)
numbers = []

for match in matches:
    numbers.append(match.group())

print(", ".join(numbers))
im