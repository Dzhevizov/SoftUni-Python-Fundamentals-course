def loading_checker(number):
    loading_bar = ['.'] * 10
    n = number // 10
    for i in range(n):
        loading_bar[i] = '%'
    loading_bar_string = "".join(loading_bar)
    if number < 100:
        print(f'{number}% [{loading_bar_string}]')
        print('Still loading...')
    else:
        print(f'{number}% Complete!')
        print(f'[{loading_bar_string}]')


loaded_percent = int(input())
loading_checker(loaded_percent)
