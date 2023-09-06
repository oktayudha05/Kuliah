with open ('pertemuan3.txt', 'r') as readfile:
    with open ('pertemuan3.txt', 'a') as writefile:
        for line in readfile:
            writefile.write(line)