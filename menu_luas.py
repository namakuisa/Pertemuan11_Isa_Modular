from luas.persegi import persegi
from luas.segitiga import segitiga
from luas.lingkaran import lingkaran
from luas.menu import menu

menu()
while 1:
    masukan = input("Masukkan pilihan: ")
    if masukan == "1":
        persegi()
    elif masukan == "2":
        lingkaran()
    elif masukan == "3":
        segitiga()
    elif masukan == "4":
        exit()
    else:
        print("Maaf, masukan Anda tidak valid")
print("Apakah Anda ingin melakukan perhitungan lagi? (Y/N)")
lagi = input().upper()
if lagi == "Y":
    menu()
else:
    print("Matematika itu menyenangkan, bukan?")