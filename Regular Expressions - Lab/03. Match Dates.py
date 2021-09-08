import re

pattern = r"\b(?P<day>\d{2})(?P<sep>[./-])(?P<month>[A-Z][a-z]{2})(?P=sep)(?P<year>\d{4})\b"
text = input()

matches = re.finditer(pattern, text)

for match in matches:
    print(f"Day: {match.group('day')}, Month: {match.group('month')}, Year: {match.group('year')}")
