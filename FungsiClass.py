class Mahasiswa:
   
    
   empCount = 0

   def __init__(self, name, salary, alamat):
      self.name = name
      self.salary = salary
      self.alamat = alamat
      Mahasiswa.empCount += 1
   
   def displayCount(self):
     print ("Total Mahasiswa %d" % Mahasiswa.empCount)

   def displayMahasiswa(self):
      print (" Name   : ", self.name ,"\n" ,"Nim    : ", self.salary, "\n" ,"Alamat : ", self.alamat  )


emp1 = Mahasiswa(input("Masukkan Nama: "), input("Masukkan NIM"), input("Masukkan Alamat"))

emp1.displayMahasiswa()