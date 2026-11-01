# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 01.11.2026
# Açıklama: Görev 4 - Collatz kaşifi. (a) Girilen n için 1'e kadar adım
# sayısını ve en yüksek değeri bulur. (b) 1'den üst sınıra kadar en uzun
# zinciri veren başlangıç sayısını iç içe döngülerle bulur.

# ---- (a) Tek bir n için ----
# 1) Girdi
n_metin = input("n: ")

# 2) Doğrula: pozitif tam sayı olmalı (isdigit eksi işareti ve harfleri kabul etmez)
if not n_metin.isdigit() or int(n_metin) < 1:
    print("Uyarı: n pozitif bir tam sayı olmalıdır.")
else:
    # 3) İşle
    n = int(n_metin)
    sayi = n
    adim = 0
    en_yuksek = n
    while sayi != 1:
        # Kural tek satırda: çiftse yarısı, tekse 3n+1
        sayi = sayi // 2 if sayi % 2 == 0 else 3 * sayi + 1
        adim += 1
        if sayi > en_yuksek:
            en_yuksek = sayi
    # 4) Çıktı
    print(f"{n} → 1: {adim} adım, en yüksek değer {en_yuksek}")

# ---- (b) 1'den üst sınıra kadar en uzun zincir ----
ust_metin = input("Üst sınır: ")

if not ust_metin.isdigit() or int(ust_metin) < 1:
    print("Uyarı: Üst sınır pozitif bir tam sayı olmalıdır.")
else:
    ust = int(ust_metin)
    en_uzun_sayi = 1
    en_uzun_adim = 0
    # Dış döngü: her başlangıç sayısını dener
    for baslangic in range(1, ust + 1):
        sayi = baslangic
        adim = 0
        # İç döngü: bu sayının zincirini 1'e kadar yürütür
        while sayi != 1:
            sayi = sayi // 2 if sayi % 2 == 0 else 3 * sayi + 1
            adim += 1
        # Daha uzun bir zincir bulduysak kaydet
        if adim > en_uzun_adim:
            en_uzun_adim = adim
            en_uzun_sayi = baslangic
    print(f"1–{ust} arasında en uzun zincir: {en_uzun_sayi} ({en_uzun_adim} adım)")
