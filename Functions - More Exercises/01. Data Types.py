def manipulate_input(tp, vl):
    if tp == 'int':
        return int(vl) * 2
    elif tp == 'real':
        return f'{float(vl) * 1.5:.2f}'
    elif tp == 'string':
        return f'${vl}$'


input_type = input()
input_value = input()
print(manipulate_input(input_type, input_value))

