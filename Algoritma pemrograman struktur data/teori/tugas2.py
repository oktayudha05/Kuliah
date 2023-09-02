tinggi = 5

for n in range(tinggi + 1):
    # membuat spasi sebelum bintang
    for s in range(tinggi - n):
        print(n, end = '')
    
    # menentukan apakah bintang atau garis bawah yang akan di tampilkan
    for o in range(2 * n - 1):
        if o % 2 == 0:
            print('*', end = '')
        else:
            print('_', end = '')
    
    # pindah baris
    print()