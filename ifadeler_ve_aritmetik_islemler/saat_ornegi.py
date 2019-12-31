# girilen saniye değerini saat dakika ve saniyeye çevireceğiz

saniye = int(input("Saniye değerini giriniz : "))

saat = saniye//3600

saniye = saniye % 3600

dakika = saniye//60

saniye = saniye%60

print(saat,"sa",dakika,"dk",saniye,"saniye")