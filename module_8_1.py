def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)

def no_zeros(x):
    if type(x) == float:
        return '{:f}'.format(x).rstrip('0').rstrip('.')
    else:
        return x

print(no_zeros(add_everything_up(123.456, 'строка')))
print(no_zeros(add_everything_up('яблоко', 4215)))
print(no_zeros(add_everything_up(123.456, 7)))