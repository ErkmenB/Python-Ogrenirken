def ListeOlustur():

    sonuc = []
    girilensayi = 0
    while girilensayi >= 0:
        girilensayi = int(input("Lütfen bir sayı giriniz (Çıkış için -1) : "))
        if girilensayi >=0:
            sonuc += [girilensayi]
    return sonuc

def main():
    sutun = ListeOlustur()
    print(sutun)

main()