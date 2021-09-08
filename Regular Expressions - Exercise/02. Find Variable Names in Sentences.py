import re

pattern = r"(^|(?<=\s))_(?P<var>[A-Za-z0-9]+)\b"
text = input()

matches = re.finditer(pattern, text)
variables = []

for match in matches:
    variables.append(match.group("var"))

print(",".join(variables))
