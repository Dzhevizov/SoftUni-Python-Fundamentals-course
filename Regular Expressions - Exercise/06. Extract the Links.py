import re

pattern = r"(?P<sub_domain>www).(?P<name>[A-Za-z0-9-]+)(?P<extension>(\.[a-z]+)+)"
text = input()

while text:

    matches = re.finditer(pattern, text)

    for match in matches:
        print(match.group())

    text = input()