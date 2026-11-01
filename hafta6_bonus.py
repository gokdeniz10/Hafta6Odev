# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 01.11.2026
# Açıklama: Bonus - Luhn algoritması. 15 haneli numaranın sonuna 0-9 arası
# rakamları sırayla ekler; numarayı geçerli yapan ilk rakamda durur.

numara = "453914880343646"

for kontrol in range(10):
    aday = numara + str(kontrol)
    toplam = 0
    # Sağdan sola gidiyoruz; sağdan 2., 4., 6. ... haneler ikiyle çarpılır
    for sira in range(len(aday)):
        hane = int(aday[len(aday) - 1 - sira])
        if sira % 2 == 1:
            hane = hane * 2
            # İki katı 9'dan büyükse rakamlarını topla (bu, 9 çıkarmakla aynı)
            if hane > 9:
                hane = hane - 9
        toplam += hane
    # Toplam 10'a tam bölünüyorsa numara geçerlidir
    if toplam % 10 == 0:
        print(f"Kontrol hanesi: {kontrol}")
        break
