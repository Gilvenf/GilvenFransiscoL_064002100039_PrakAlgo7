print("PROGRAM MENCARI NILAI FAKTORIAL DARI SEBUAH ANGKA")
angka=int(input("Masukkan Angka: "))
def faktorial(angka):
    faktorial= 1
    for i in range(1,angka+1):
        faktorial=faktorial*i
    return faktorial
faktorial_bilangan=faktorial(angka)
print("Nilai Faktorial nya adalah",faktorial_bilangan)