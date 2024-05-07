Berat_Badan = int(input("Masukkan Berat Badan : "))
Tinggi_Badan = int(input("Masukkan Tinggi Badan : "))

Pembagian = Berat_Badan/Tinggi_Badan
print(Pembagian)

if Berat_Badan <= 18.5:
   print("Berat Badan Kurang")

if Berat_Badan <= 24.9:
     print("Berat Badan Normal")
if Berat_Badan <= 29.9:
     print("Kelebihan Berat Badan")
else:
     print("Obesitas")