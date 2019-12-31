from tkinter import Tk, Canvas
from tkinter.ttk import Button, Frame
def Butonabasildiginda():
    global renk
    if renk == "red":
        renk =="green"
        canvas.itemconfigure(kirmizilamba,fill="black")       #Kırmızı ışık kapatılıyor.
        canvas.itemconfigure(yesillamba,fill="green")         #Yeşil lamba yanıyor.
    elif renk == "green" :
        renk == "yellow"
        canvas.itemconfigure(yesillamba,fill="black")         #Yeşil lamba kapatılıyor.
        canvas.itemconfigure(sarilamba,fill="yellow")         #Sarı lamba yanıyor.
    elif renk == "yellow":
        renk == "red"
        canvas.itemconfigure(sarilamba,fill="black")          #Sarı lamba kapatılıyor.
        canvas.itemconfigure(kirmizilamba,fill="red")         #Kırmızı lamba kapatılıyor.

    #Kullanılacak değişkenler tanımlanıyor.

    renk == "red"    #açık olarak gelecek ilk ışık kırmızı.
root = Tk()     #ana pencerenin oluşturulması
root.title("Trafik ışıkları")   #Pencere başlığı
frame = Frame(root)     #Nesnelerin birlikte tutulması için frame oluşturuluyor.
frame.pack()            #Pencere içerisine frame yerleştiriliyor.

#Grafiksel birimlerin yerleştirileceği çizim alanı (canvas) oluşturuluyor.

canvas = Canvas(frame, width=150, height=300)

canvas.create_rectangle(50,20,150,280,fill="gray")
kirmizilamba = canvas.create_oval(70,40,130,100,fill="red")
sarilamba = canvas.create_oval(70,120,130,180,fill="black")
yesillamba = canvas.create_oval(70,200,130,260,fill="black")

button = Button(frame, text="Değiştir", command = Butonabasildiginda)

button.grid(row=0, column=0)
canvas.grid(row=0, column=1)

root.mainloop()
