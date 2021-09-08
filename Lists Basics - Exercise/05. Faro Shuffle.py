list_of_cards = input().split(" ")
shuffles = int(input())

list1 = []
list2 = []

for i in range(shuffles):
    list1 = list_of_cards[:(len(list_of_cards)//2)]
    list2 = list_of_cards[(len(list_of_cards)//2):]
    k = 0
    for j in range(0, len(list_of_cards), 2):
        list_of_cards[j] = list1[k]
        list_of_cards[j + 1] = list2[k]
        k += 1

print(list_of_cards)