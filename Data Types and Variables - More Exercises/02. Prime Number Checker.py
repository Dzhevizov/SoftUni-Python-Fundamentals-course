number = int(input())
is_prime = True

if number <= 1:
    is_prime = False
elif not number % 2:
    is_prime = False
else:
    for i in range(3, number, 2):
        if not number % i:
            is_prime = False

print(is_prime)