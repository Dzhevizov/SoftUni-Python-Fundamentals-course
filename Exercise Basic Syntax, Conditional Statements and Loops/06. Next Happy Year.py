year = int(input())
distinct = False
while not distinct:
    year += 1
    if len(set(str(year))) == len(str(year)):
        distinct = True
print(year)