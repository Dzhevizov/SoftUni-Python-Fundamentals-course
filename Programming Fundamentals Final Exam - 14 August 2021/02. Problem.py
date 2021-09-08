import re

num_of_lines = int(input())

pattern = r"(?P<surr>\*|\@)(?P<tag>[A-Z][a-z]{2,})(?P=surr): \[(?P<group1>[A-Za-z])\]\|\[(?P<group2>[A-Za-z])\]\|\[(?P<group3>[A-Za-z])\]\|(?=$)"

for _ in range(num_of_lines):

    line = input()
    matches = re.finditer(pattern, line)

    count = 0

    for match in matches:

        count += 1

        tag = match.group('tag')
        num1 = ord(match.group('group1'))
        num2 = ord(match.group('group2'))
        num3 = ord(match.group('group3'))

        print(f"{tag}: {num1} {num2} {num3}")

    if not count:
        print("Valid message not found!")
