def print_trib_rec(num):
    if num == 1 or num == 2:
        return 1
    elif num == 3:
        return 2
    else:
        return (print_trib_rec(num - 1) +
                print_trib_rec(num - 2) +
                print_trib_rec(num - 3))


def print_trib(num):
    for i in range(1, num + 1):
        print(print_trib_rec(i), end=" ")


number = int(input())
print_trib(number)