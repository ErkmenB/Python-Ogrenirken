from tkinter import Tk, Button, Label

sayac = 0  # tıklanma sayısını hafızada tutacak değişken tanımlanıyor.

def update():
    #butona tıklandıkça sayaç arttırma işlemi

    global sayac,b,etiket
    sayac+=1
    b.config(text="Tıklanma sayısı = "+ str(sayac))
    print("Güncelleniyor...")

root = Tk()
b = Button(root)
b.configure(background = "yellow", text = "Tıklanma sayısı = 0", command = update)

b.pack()
root.mainloop()