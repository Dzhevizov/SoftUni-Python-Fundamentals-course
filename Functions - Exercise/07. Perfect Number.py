def perfect_num_finder(number):
    sum_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_divisors += i
    if sum_divisors == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


input_num = int(input())
perfect_num_finder(input_num)