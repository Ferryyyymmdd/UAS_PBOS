class kalkulator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def tambah(self):
        return self.a + self.b
    def kurang(self):
        return self.a - self.b
    def perkalian(self):
        return self.a * self.b
    def bagi(self):
        return self.a // self.b
    
nilai = kalkulator((int(input("Masukkan Nilai Ke 1: "))),(int(input("Masukkan Nilai Ke 2 : "))))

hasil = nilai.tambah()
print("Operasi Penjumlahan",hasil)

hasil = nilai.kurang()
print("Operasi Pengurangan",hasil)

hasil = nilai.perkalian()
print("Operasi Perkalian",hasil)

hasil = nilai.bagi()
print("Operasi Pembagian",hasil)
    
