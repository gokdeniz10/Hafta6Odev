# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 01.11.2026
# Açıklama: Görev 2 - Metin analizörü. Bir cümlede tek bir for döngüsüyle harf,
# sesli, sessiz, rakam ve kelime sayısını bulur; cümleyi ters yazar ve
# palindrom olup olmadığını söyler.

# 1) Girdi
cumle = input("Cümle: ")

# 2) Doğrula: boş cümle girilmesin
if cumle.strip() == "":
    print("Uyarı: Boş bir cümle girdiniz.")
else:
    # Sayaçlar
    harf = 0
    sesli = 0
    sessiz = 0
    rakam = 0
    kelime = 0
    # Bayrak: şu an bir kelimenin içinde miyiz?
    kelime_icinde = False
    # Ters cümle ve palindrom kontrolü için biriktirdiğimiz metinler
    ters = ""
    harfler = ""        # sadece harfler, küçük harfle, düz sırada
    ters_harfler = ""   # sadece harfler, küçük harfle, ters sırada

    # 3) İşle: tek döngü
    for karakter in cumle:
        # Her karakteri başa ekleyince cümle ters dönmüş olur
        ters = karakter + ters

        if karakter.isalpha():
            harf += 1
            # Türkçe büyük İ ve I harflerini doğru küçült
            if karakter == "İ":
                kucuk = "i"
            elif karakter == "I":
                kucuk = "ı"
            else:
                kucuk = karakter.lower()
            harfler = harfler + kucuk
            ters_harfler = kucuk + ters_harfler
            if kucuk in "aeıioöuü":
                sesli += 1
            else:
                sessiz += 1
        elif karakter.isdigit():
            rakam += 1

        # Kelime sayma: boşluk görünce kelime biter, boşluk olmayan bir
        # karaktere ilk kez gelince yeni kelime başlar.
        if karakter == " ":
            kelime_icinde = False
        elif not kelime_icinde:
            kelime_icinde = True
            kelime += 1

    # 4) Çıktı
    print(f"Harf: {harf}  Sesli: {sesli}  Sessiz: {sessiz}  Rakam: {rakam}  Kelime: {kelime}")
    print(f"Ters: {ters}")
    if harfler == ters_harfler:
        print("Palindrom")
    else:
        print("Palindrom değil")
