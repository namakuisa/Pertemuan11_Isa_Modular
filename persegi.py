from luas.menu import menu

def persegi():
    print("Menghitung Luas Persegi Panjang")
    p = float(input("Masukkan Panjang : "))
    l = float(input("Masukkan Lebar : "))
    luas = p*l
    print("Luas Persegi Panjang adalah ",luas)
    print()
    print("Apakah Anda ingin melakukan perhitungan lagi? (Y/N)")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        print("Matematika itu menyenangkan, bukan?")
        exit()