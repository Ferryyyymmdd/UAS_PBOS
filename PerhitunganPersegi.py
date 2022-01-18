def Hitung_Luas():
    p = int(input("Masukkan Nilai Panjang : "))
    L = int(input("Masukkan Nilai Lebar : "))
    luas = p * L
    print("Luas Persegi Panjang = " +str(luas))
    
def Hitung_Keliling():
    p = int(input("Masukkan Nilai Panjang : "))
    L = int(input("Masukkan Nilai Lebar : "))
    Keliling = p + L + p + L
    print("Keliling Persegi Panjang = " +str(Keliling))

def show_menu():
    print("\n")
    print("_______Menu_______")
    print("(1) Hitung Luas")
    print("(2) Hitung Keliling")
    print("(3) Exit")

    menu = input("pilih menu")
    print("\n")

    if menu == "1" :
        Hitung_Luas()
    if menu == "2" :
        Hitung_Keliling()
    if menu == "3" :
        exit()

    else:
        print("salah pilih")

if __name__ == "__main__":
    while(True):
        show_menu()