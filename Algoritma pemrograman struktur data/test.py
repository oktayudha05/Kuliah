tinggi = 5

for n_tinggi in range(tinggi):
    for j in range(n_tinggi, tinggi):
        print(' ', end='')
    
    for j in range(n_tinggi):
        print('*', end=' ')

    print()