import re

pattern = r"(^|(?<=\s))(?P<user>[A-Za-z0-9]+[-._]*[A-Za-z0-9]+)@(?P<host>([A-Za-z]+[-]*[A-Za-z]+[.]+[A-Za-z]+[-]*[A-Za-z]+([.][a-z]+)*)+)"
text = input()

matches = re.finditer(pattern, text)

for match in matches:
    print(f"{match.group('user')}@{match.group('host')}")
