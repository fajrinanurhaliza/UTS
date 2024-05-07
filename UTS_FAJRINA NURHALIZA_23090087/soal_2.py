def tahun_kabisat(tahun):
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        return True
    else:
        return False

tahun = int(input("Masukkan tahun: "))

if tahun_kabisat(tahun):
    print(f"tahun {tahun} Tahun Kabisat")
else:
    print(f"tahun {tahun} Bukan Tahun Kabisat")