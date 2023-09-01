tinggi = 5

for n in range(1,tinggi+1):
    for j in range(tinggi-n):
        print(' ', end='')
    
    for j in range(2 * n - 1):
        if j % 2 == 0:
            print('*', end='')
        else:
            print('_', end='')

    print()