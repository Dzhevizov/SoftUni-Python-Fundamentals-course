first_line = input().split()
second_line = input().split()
third_line = input().split()

is_winner = False


def check_line(line):
    global is_winner
    if line[0] == line[1] == line[2]:
        if line[0] == '1':
            print('First player won')
            is_winner = True
        elif line[0] == '2':
            print('Second player won')
            is_winner = True


def check_column(num):
    global is_winner
    if first_line[num] == second_line[num] == third_line[num]:
        if first_line[num] == '1':
            print('First player won')
            is_winner = True
        elif first_line[num] == '2':
            print('Second player won')
            is_winner = True


def check_first_diagonal():
    global is_winner
    if first_line[0] == second_line[1] == third_line[2]:
        if first_line[0] == '1':
            print('First player won')
            is_winner = True
        elif first_line[0] == '2':
            print('Second player won')
            is_winner = True


def check_second_diagonal():
    global is_winner
    if first_line[2] == second_line[1] == third_line[0]:
        if first_line[2] == '1':
            print('First player won')
            is_winner = True
        elif first_line[2] == '2':
            print('Second player won')
            is_winner = True


check_line(first_line)
check_line(second_line)
check_line(third_line)
check_column(0)
check_column(1)
check_column(2)
check_first_diagonal()
check_second_diagonal()

if not is_winner:
    print('Draw!')
