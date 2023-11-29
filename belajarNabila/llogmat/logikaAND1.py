import coba as pilihan

hasil_input = pilihan.pilihan()

def gerbang_and(input1, input2):
    if input1 and input2 == False:
        print(f"Hasil AND dari {input1} dan {input2} adalah False")
    elif input1 and input2 == True:
        print(f"Hasil AND dari {input1} dan {input2} adalah True")   

if hasil_input == '1':
    input1 = input('masukan p: ')
    input2 = input('masukan q: ')
    i_bool = input1 != "0"
    j_bool = input2 != "0"
    print(i_bool)
    print(j_bool)
    gerbang_and(i_bool, j_bool)

