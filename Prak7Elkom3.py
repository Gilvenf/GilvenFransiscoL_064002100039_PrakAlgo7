print("PROGRAM PENGENCEKAN BILANGAN")
bilangan=int(input("Masukkan bilangan: "))
def kubik(angka):
    angka**3
    print("hasil:",angka**3)
def angka(bilangan):
    if bilangan%3==0:
        kubik(bilangan)
    else :
        print("Hasil:False")
angka(bilangan)