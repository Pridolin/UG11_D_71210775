#input data 
a = input("Masukkan sebuah kata/kalimat : ")
b = input ("Masukkan karakter yang ingin disisipkan : ")

def sisipHuruf() :
    print(b.join(a.upper()))
def sisipKata() :
    print(a.join(b))


sisipHuruf()
sisipKata()