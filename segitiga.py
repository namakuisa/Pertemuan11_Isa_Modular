from luas.menu import menu

def segitiga():
    print("Menghitung Luas Segitiga")
    a = float(input("Masukkan Alas : "))
    t = float(input("Masukkan Tinggi : "))
    luas = (a*t)/2
    print("Luas Segitiga adalah ",luas)
    print()
    print("Apakah Anda ingin melakukan perhitungan lagi? (Y/N)")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        print("Matematika itu menyenangkan, bukan?")
        exit()