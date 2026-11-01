# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 01.11.2026
# Açıklama: Görev 5 - Adam asmaca. Gizli kelimeyi harf harf tahmin ettirir.
# Denenen harfler bir karakter dizisinde birikir. 6 hata hakkı vardır.

gizli = "KOŞUL"
tahminler = ""   # denenen harfler burada birikir
hata = 0

while hata < 6:
    # Kelimeyi "K _ Ş U _" biçiminde hazırla ve eksik harfleri say
    gorunen = ""
    eksik = 0
    for h in gizli:
        if gorunen != "":
            gorunen += " "
        if h in tahminler:
            gorunen += h
        else:
            gorunen += "_"
            eksik += 1

    # Eksik harf kalmadıysa kazandık
    if eksik == 0:
        print(f"{gorunen}   (hata: {hata}/6)   Kazandınız!")
        break

    print(f"{gorunen}   (hata: {hata}/6)")

    # Girdi
    harf = input("Harf: ")

    # Doğrula: tek bir harf olmalı
    if len(harf) != 1 or not harf.isalpha():
        print("→  Lütfen tek bir harf girin.")
        continue

    # "i".upper() Türkçe İ değil I verdiği için i harfini elle çeviriyoruz
    if harf == "i":
        harf = "İ"
    else:
        harf = harf.upper()

    # Doğrula: daha önce denendi mi?
    if harf in tahminler:
        print("→  Bu harfi zaten denediniz.")
        continue

    # İşle: harfi kaydet, kelimede yoksa hata say
    tahminler += harf
    if harf not in gizli:
        hata += 1
else:
    # break olmadan çıkıldıysa 6 hata dolmuştur
    print(f"(hata: {hata}/6)   Kaybettiniz! Kelime: {gizli}")
