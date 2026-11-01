# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 01.11.2026
# Açıklama: Görev 1 - Üçgen analizörü. Üç kenarı okur, üçgen olup olmadığını
# kontrol eder; üçgeni kenarlarına ve en büyük açısına göre sınıflandırır,
# çevreyi, alanı (Heron) ve en büyük açıyı yazdırır.

import math

# 1) Girdi: üç kenarı oku
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# 2) Doğrula: kenarlar pozitif mi, üçgen eşitsizliği sağlanıyor mu?
if a <= 0 or b <= 0 or c <= 0:
    print("Uyarı: Kenar uzunlukları pozitif olmalıdır.")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Uyarı: Bu kenarlarla üçgen olmaz (üçgen eşitsizliği sağlanmıyor).")
else:
    # 3) İşle
    # Formülde a en uzun kenar olmalı. b ya da c daha uzunsa a ile yer değiştir.
    if b > a:
        gecici = a
        a = b
        b = gecici
    if c > a:
        gecici = a
        a = c
        c = gecici

    # Kenarlara göre tür
    if a == b and b == c:
        kenar_turu = "Eşkenar"
    elif a == b or b == c or a == c:
        kenar_turu = "İkizkenar"
    else:
        kenar_turu = "Çeşitkenar"

    # En büyük açı: en uzun kenarın (a) karşısındaki açı
    cos_aci = (b * b + c * c - a * a) / (2 * b * c)
    aci = math.degrees(math.acos(cos_aci))

    # Açıya göre tür. 90 ile == ile karşılaştırmıyoruz, çünkü ondalıklı
    # hesapta 89.99999 gibi küçük farklar çıkabilir. isclose bunu tolere eder.
    if math.isclose(aci, 90):
        aci_turu = "Dik"
    elif aci > 90:
        aci_turu = "Geniş"
    else:
        aci_turu = "Dar"

    # Çevre ve Heron formülü ile alan (u = yarı çevre)
    cevre = a + b + c
    u = cevre / 2
    alan = math.sqrt(u * (u - a) * (u - b) * (u - c))

    # 4) Çıktı
    print(f"Tür: {kenar_turu}, {aci_turu} açılı")
    print(f"Çevre: {cevre:.2f}   Alan: {alan:.2f}   En büyük açı: {aci:.2f}°")
