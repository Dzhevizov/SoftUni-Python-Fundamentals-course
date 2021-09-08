import sys


def exchange_command(string1, list1):
    index = int(string1.split()[1])
    if index not in range(len(list1)):
        print("Invalid index")
    else:
        left_list = list1[:index + 1]
        right_list = list1[index + 1:]
        list1 = right_list + left_list
    return list(map(int, list1))


def max_command(string1, list1):
    max_el = -sys.maxsize
    element_type = string1.split()[1]
    if element_type == "even":
        for element in list1:
            if int(element) % 2 == 0 and int(element) >= int(max_el):
                max_el = element
    else:
        for element in list1:
            if not int(element) % 2 == 0 and int(element) >= int(max_el):
                max_el = element
    if int(max_el) == -sys.maxsize:
        print("No matches")
    else:
        index = 0
        for i in range(len(list1)):
            if list1[i] == max_el:
                index = i
        print(index)


def min_command(string1, list1):
    min_el = sys.maxsize
    element_type = string1.split()[1]
    if element_type == "even":
        for element in list1:
            if int(element) % 2 == 0 and int(element) <= int(min_el):
                min_el = element
    else:
        for element in list1:
            if not int(element) % 2 == 0 and int(element) <= int(min_el):
                min_el = element
    if int(min_el) == sys.maxsize:
        print("No matches")
    else:
        index = 0
        for i in range(len(list1)):
            if list1[i] == min_el:
                index = i
        print(index)


def first_command(string1, list1):
    count = string1.split()[1]
    element_type = string1.split()[2]
    if int(count) > len(list1):
        print("Invalid count")
    else:
        list_res = []
        if element_type == "even":
            for element in list1:
                if int(element) % 2 == 0:
                    list_res.append(element)
                    if len(list_res) == int(count):
                        break
        else:
            for element in list1:
                if not int(element) % 2 == 0:
                    list_res.append(element)
                    if len(list_res) == int(count):
                        break
        print(list(map(int, list_res)))


def last_command(string1, list1):
    count = string1.split()[1]
    element_type = string1.split()[2]
    list2 = list1[::-1]
    if int(count) > len(list2):
        print("Invalid count")
    else:
        list_res = []
        if element_type == "even":
            for element in list2:
                if int(element) % 2 == 0:
                    list_res.append(element)
                    if len(list_res) == int(count):
                        break
        else:
            for element in list2:
                if not int(element) % 2 == 0:
                    list_res.append(element)
                    if len(list_res) == int(count):
                        break
        list_res1 = list_res[::-1]
        print(list(map(int, list_res1)))


input_list = input().split()
command = ""

while not command == "end":
    command = input()
    if "exchange" in command:
        input_list = exchange_command(command, input_list)
    elif "max" in command:
        max_command(command, input_list)
    elif "min" in command:
        min_command(command, input_list)
    elif "first" in command:
        first_command(command, input_list)
    elif "last" in command:
        last_command(command, input_list)

print(list(map(int, input_list)))
