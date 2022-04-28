import numpy as np
from collections import OrderedDict
import re

alfabe = [
    "a","b","c","ç","d",
    "e","f","g","ğ","h",
    "ı","i","j","k","l",
    "m","n","o","ö","p",
    "r","ş","s","t","u",
    "ü","v","y","z"
]


def kaydirma():
    sifrelenecekCumle = input("Şifrelenecek cümle:")
    kaydirilacakDeger = int(input("Kaydırılacak değer:"))
    yeniAlfabe = []
    eksikKisim = []
    for c in range(len(alfabe)):
        if c >= kaydirilacakDeger:
            yeniAlfabe.append(alfabe[c])
        elif c < kaydirilacakDeger:
            eksikKisim.append(alfabe[c])
    for c in eksikKisim:
        yeniAlfabe.append(c)

    sifreliCumle = sifrele(sifrelenecekCumle, yeniAlfabe)

    print(sifreliCumle)
    


def anahtarliKaydirma():
    anahtar = input("Anahtar girin:")
    sifrelenecekCumle = input("Şifrelenecek cümle:")
    unique = []
    sonAlfabe = []

    for c in anahtar:
        if not c in unique:
            unique.append(c)
    for c in unique:
        sonAlfabe.append(c)
    for c in alfabe:
        if not c in anahtar:
            sonAlfabe.append(c)
    sifreliCumle = sifrele(sifrelenecekCumle, sonAlfabe)

    print(sifreliCumle)

def sifrele(sifrelenecekCumle, sonAlfabe):
    sifreliCumle = ""
    for c in sifrelenecekCumle:
        if (ord(c) == 97):
            sifreliCumle += sonAlfabe[0]
        elif (ord(c) == 98):
            sifreliCumle += sonAlfabe[1]
        elif (ord(c) == 99):
            sifreliCumle += sonAlfabe[2]
        elif (ord(c) == 231):
            sifreliCumle += sonAlfabe[3]
        elif (ord(c) == 100):
            sifreliCumle += sonAlfabe[4]
        elif (ord(c) == 101):
            sifreliCumle += sonAlfabe[5]
        elif (ord(c) == 102):
            sifreliCumle += sonAlfabe[6]
        elif (ord(c) == 103):
            sifreliCumle += sonAlfabe[7]
        elif (ord(c) == 287):
            sifreliCumle += sonAlfabe[8]
        elif (ord(c) == 104):
            sifreliCumle += sonAlfabe[9]
        elif (ord(c) == 305):
            sifreliCumle += sonAlfabe[10]
        elif (ord(c) == 105):
            sifreliCumle += sonAlfabe[11]
        elif (ord(c) == 106):
            sifreliCumle += sonAlfabe[12]
        elif (ord(c) == 107):
            sifreliCumle += sonAlfabe[13]
        elif (ord(c) == 108):
            sifreliCumle += sonAlfabe[14]
        elif (ord(c) == 109):
            sifreliCumle += sonAlfabe[15]
        elif (ord(c) == 110):
            sifreliCumle += sonAlfabe[16]
        elif (ord(c) == 111):
            sifreliCumle += sonAlfabe[17]
        elif (ord(c) == 246):
            sifreliCumle += sonAlfabe[18]
        elif (ord(c) == 112):
            sifreliCumle += sonAlfabe[19]
        elif (ord(c) == 113):
            sifreliCumle += sonAlfabe[20]
        elif (ord(c) == 114):
            sifreliCumle += sonAlfabe[21]
        elif (ord(c) == 115):
            sifreliCumle += sonAlfabe[22]
        elif (ord(c) == 351):
            sifreliCumle += sonAlfabe[23]
        elif (ord(c) == 116):
            sifreliCumle += sonAlfabe[24]
        elif (ord(c) == 117):
            sifreliCumle += sonAlfabe[25]
        elif (ord(c) == 252):
            sifreliCumle += sonAlfabe[26]
        elif (ord(c) == 118):
            sifreliCumle += sonAlfabe[27]
        elif (ord(c) == 121):
            sifreliCumle += sonAlfabe[28]

    return sifreliCumle



def kirilamayan_sifre_5_2_decrypt():
    anahtar = input("Şifre için anahtar girin:")
    tablo = [["" for x in range(len(alfabe))] for y in range(len(anahtar))]
    for i in range(len(anahtar)):
        kayitEdilsinmi = False
        sarkma = 0
        for j in range(len(alfabe)):
            if (alfabe[j] == anahtar[i]):
                kayitEdilsinmi = True
                sarkma = j
            if (kayitEdilsinmi):
                tablo[i][j - sarkma] = alfabe[j]

        for x in range(sarkma):
            tablo[i][len(alfabe) - (sarkma - x)] = alfabe[x]

    sifrelenmisMesaj = input("Şifrelenen mesajı girin: ")
    cozulmusMesaj = ""

    for i in range(len(sifrelenmisMesaj)):
        anahtarIndis = i%4
        cozulmusIndis = 0
        for j in range(len(alfabe)):
            if(tablo[anahtarIndis][j] == sifrelenmisMesaj[i]):
                cozulmusIndis = j
                break
        cozulmusMesaj = cozulmusMesaj + alfabe[j]
    print(cozulmusMesaj)

def kirilamayan_sifre_5_2_encrypt():
    anahtar = input("Şifre için anahtar girin:")
    tablo = [["" for x in range(len(alfabe))] for y in range(len(anahtar))]
    for i in range(len(anahtar)):
        kayitEdilsinmi = False
        sarkma = 0
        for j in range(len(alfabe)):
            if(alfabe[j] == anahtar[i]):
                kayitEdilsinmi = True
                sarkma = j
            if(kayitEdilsinmi):
                tablo[i][j - sarkma] = alfabe[j]

        for x in range(sarkma):
            tablo[i][len(alfabe) - (sarkma - x) ] = alfabe[x]

    sifrelenecekMesaj = input("Şifrelenecek mesajı girin: ")
    sifrelenmisMesaj = ""

    for i in range(len(sifrelenecekMesaj)):
        harfIndis = 0
        anahtarIndis = i%4
        for j in range(len(alfabe)):
            if(alfabe[j] == sifrelenecekMesaj[i]):
                harfIndis = j
                break
        sifrelenmisMesaj = sifrelenmisMesaj + tablo[anahtarIndis][harfIndis]

    print(sifrelenmisMesaj)


def matris_tersi():
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    d = int(input("d:"))
    z = int(input("z tabanı:"))
    tablo = [
        [a,b],
        [c,d]
    ]
    determinant = ((a * d) - (b * c))

    if determinant == 0:
        print("Matrisin tersi yoktur..")
        return

    determinant = determinant%z

    tersDeterminant = 0
    for x in range(z):
        if (determinant * x)%z == 1:
            tersDeterminant = x
            break

    yeniTablo = [
        [((tablo[1][1]) * tersDeterminant)%z,((-1 * (tablo[0][1])) * tersDeterminant)%z],
        [((-1 * tablo[1][0]) * tersDeterminant)%z,(tablo[0][0] * tersDeterminant)%z]
    ]

    a = ""
    for i in range(2):
        a = a + "[ "
        for j in range(2):
            a = a + str(yeniTablo[i][j]) + " "
        a = a + "]\n"
    print(a)

def hill_sifreleme_encrypt():
    aktif_terslenebilir_matris = [
        [2,3],
        [4,5]
    ]
    sifrelenecek_metin = input("Şifrelenecek metin:")
    z = int(input("z:"))
    bloklar = []
    metin_dizi = re.findall("..",sifrelenecek_metin)
    for i in range(len(metin_dizi)):
        blok = [0,0]
        saydirgac = 0
        for j in range(len(alfabe)):
            if(metin_dizi[i][0] == alfabe[j]):
                blok[0] = j
                saydirgac = saydirgac + 1
            if(metin_dizi[i][1] == alfabe[j]):
                blok[1] = j
                saydirgac = saydirgac + 1
            if(saydirgac >= 2):
                break
        bloklar.append(blok)

    sifrelenmis_metin = ""

    for i in range(len(bloklar)):

        a = ((aktif_terslenebilir_matris[0][0] * bloklar[i][0]) + (aktif_terslenebilir_matris[0][1] * bloklar[i][1]))%z
        b = ((aktif_terslenebilir_matris[1][0] * bloklar[i][0]) + (aktif_terslenebilir_matris[1][1] * bloklar[i][1]))%z

        bloklar[i][0] = a
        bloklar[i][1] = b

        sifrelenmis_metin = sifrelenmis_metin + alfabe[bloklar[i][0]] + alfabe[bloklar[i][1]]

    print(sifrelenmis_metin)




def main():
    while(True):
        print("------------------")
        print("A - Kaydırma")
        print("B - Anahtar Kaydırma")
        print("C - Kırılamayan şifre (DAYI ÖRNEĞİ) şifreleme")
        print("D - Kırılamayan şifre (DAYI ÖRNEĞİ) çözme")
        print("E - Matris tersi")
        print("F - Hill Şifreleme")
        print("(Diğer) - Çıkış")
        print("------------------")
        secim = input("Seçim:")
        if secim.lower() == "a":
            kaydirma()
        elif secim.lower() == "b":
            anahtarliKaydirma()
        elif secim.lower() == "c":
            kirilamayan_sifre_5_2_encrypt()
        elif secim.lower() == "d":
            kirilamayan_sifre_5_2_decrypt()
        elif secim.lower() == "e":
            matris_tersi()
        elif secim.lower() == "f":
            hill_sifreleme_encrypt()
        else:
            break
        x = input("Bir tuşa basın..")
main()