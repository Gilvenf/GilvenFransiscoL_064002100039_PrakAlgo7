print("MENGHITUNG HURUF VOKAL DAN KONSONAN")
kalimat=input("Masukkan Kalimat: ")
def isvokal(kalimat):
    hvokal=0
    hkonsonan=0
    kalimat=kalimat.lower()
    for i in kalimat:
        if i in["a","i","u","e","o"]:
            hvokal+=1
        elif i in["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]:
            hkonsonan+=1
    print("Jumlah Vokal :",hvokal)
    print("Jumlah Konsonan :",hkonsonan)
isvokal(kalimat)
