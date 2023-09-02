tinggi = 5

for n in range(1, tinggi + 1):
    # membuat spasi sebelum bintang
    for s in range(tinggi - n):
        print(' ', end = '')
    
    # menentukan apakah bintang atau garis bawah yang akan di tampilkan
    for s in range(n * 2 - 1):
        if s % 2 == 0:
            print('*', end = '')
        else:
            print('_', end = '')
    
    # pindah baris
    print()