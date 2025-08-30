#1.SORU

sayi = int(input("Bir sayı giriniz: "))

if sayi % 2 == 0:
    a = " Çift "
else:
    a = " Tek "
    
if sayi > 0:
    print("Pozitif" + a + "Sayı")
elif sayi < 0:
    print("Negatif" + a + "Sayı")
else:
    print("Sıfır")
print()

  
#2.SORU

kelime = input("Bir kelime giriniz: ")

sonuc = {}

for i in range(len(kelime)):
    if kelime[i] in sonuc:
        sonuc[kelime[i]] += 1
    else:
        sonuc[kelime[i]] = 1

print(sonuc)
print()


#3.SORU

sifre = input("Şifrenizi giriniz: ")

uzunluk_bool = len(sifre) >= 8

buyuk_harf_bool = False

for a in sifre:
    if a.isupper():
        buyuk_harf_bool = True
        break
    
rakam_bool = False

for a in sifre:
    if a.isdigit():
        rakam_bool = True
        break
    
if uzunluk_bool and buyuk_harf_bool and rakam_bool:
    print("Şifre geçerli")
else:
    if not uzunluk_bool:
        print("En az 8 karakter olmalı")
    if not buyuk_harf_bool:
        print("En az 1 büyük harf içermeli")
    if not rakam_bool:
        print("En az 1 rakam içermeli")
print()


#4.SORU

lst = [12, 4, 9, 25, 30, 7, 18] 

ort = sum(lst) / len(lst)

buyuk_sayılar = []

for a in lst:
    if a > ort:
        buyuk_sayılar.append(a)
        
print("Ortalama:", ort)
print("Ortalamadan büyük sayılar:", buyuk_sayılar)
print()


#5.SORU

for i in range(1,6):
    print("*" * i)
    print()
    
    
#6.SORU

toplam = 0
sayı_miktarı = 0

while True:
    sayi = int(input("Bir sayı giriniz (İşlemi sonlandırmak için '0' giriniz): "))
    if sayi == 0:
        break
    toplam += sayi
    sayı_miktarı +=1

if sayı_miktarı == 0:
    print("Sayı girmeden bitirdiniz.")
else:
    ort = toplam / sayı_miktarı
    print("Toplam: ", toplam)
    print("Ortalama: ", ort)
print()
    

#7.SORU

kelime = input("Bir kelime giriniz: ")

ters_kelime = kelime[::-1]

if kelime == ters_kelime:
    print(kelime + " Palindromdur.")
else:
    print(kelime + " Palindrom değildir.")
print()
    

#8.SORU

sonuc = []

for sayi in range(1,101):
    if sayi % 3 == 0 and sayi % 5 == 0:
        sayi_karesi = sayi ** 2
        sonuc.append(sayi_karesi)
        
print("1-100 arası hem 3'e hem 5'e bölünebilen sayıların kareleri: ", sonuc)
print()


#9.SORU

cumle = input("Bir cümle giriniz: ")

kelimeler = cumle.split()

buyuk_kelimeler = []

for kelime in kelimeler:
    k = kelime[0].upper() + kelime[1:]
    buyuk_kelimeler.append(k)
    
son_cumle = " ".join(buyuk_kelimeler)
print(son_cumle)
print()


#MİNİ PROJE

yorumlar = []

while True:
    yorum = input("Bir film yorumu giriniz (İşlemi sonlandırmak için '0' giriniz.): ")
    if yorum.lower() == "0":
        break
    yorumlar.append(yorum)
    
toplam_yorum_sayısı = len(yorumlar)

iyi_sayisi = 0

for yorum in yorumlar:
    if "iyi" in yorum.lower():
        iyi_sayisi += 1
        
en_uzun_yorum = max(yorumlar, key=len)
en_kısa_yorum = min(yorumlar, key=len)

toplam_uzunluk = 0

for yorum in yorumlar:
    toplam_uzunluk += len(yorum)

ort_uzunluk = toplam_uzunluk / toplam_yorum_sayısı

print("\nToplam yorum sayısı: ", toplam_yorum_sayısı)
print("'iyi' geçen yorum sayısı: ", iyi_sayisi)
print("En uzun yorum: ", en_uzun_yorum)
print("En kısa yorum: ", en_kısa_yorum)
print("Ortalama uzunluk: ", ort_uzunluk)