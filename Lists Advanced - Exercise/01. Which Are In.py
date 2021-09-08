list1 = input().split(", ")
list2 = input().split(", ")
list_res = []
for x in list1:
    for y in list2:
        if x in y:
            list_res.append(x)
            break
print(list_res)