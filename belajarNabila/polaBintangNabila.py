a = 5


for s in range(a+1):
    for u in range(a-s):
        print(' ', end='')

    for n in range(2 * s - 1):
        if n % 2 == 0:
            print('*', end='')
        else:
            print('_', end='')

    print()