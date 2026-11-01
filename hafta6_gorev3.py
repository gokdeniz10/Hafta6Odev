# Ad Soyad: Gökdeniz Demirbağ
# Öğrenci No: 20253004005
# Tarih: 01.11.2026
# Açıklama: Görev 3 - T.C. kimlik numarası doğrulama. Numaranın biçimini
# kontrol eder, iki kontrol hanesini hesaplar ve numaranın geçerli olup
# olmadığını yazar. Sadece test numaraları kullanılmalıdır.

# 1) Girdi: numarayı metin olarak oku (başındaki sıfır kaybolmasın diye)
tc = input("T.C. kimlik no: ")

# 2) Doğrula: 11 karakter, hepsi rakam, ilk hane 0 değil
if len(tc) != 11 or not tc.isdigit() or tc[0] == "0":
    print("→  GEÇERSİZ")
else:
    # 3) İşle: 1-9. haneleri dolaş
    tek = 0    # 1., 3., 5., 7., 9. hanelerin toplamı (T)
    cift = 0   # 2., 4., 6., 8. hanelerin toplamı (Ç)
    for sira in range(9):
        hane = int(tc[sira])
        # sira 0'dan başlar: sira 0, 2, 4... hanenin 1., 3., 5. olduğu anlamına gelir
        if sira % 2 == 0:
            tek += hane
        else:
            cift += hane

    hane10 = (7 * tek - cift) % 10
    hane11 = (tek + cift + hane10) % 10

    # 4) Çıktı: hesaplanan haneler numaradakilerle aynı mı?
    if hane10 == int(tc[9]) and hane11 == int(tc[10]):
        print(f"Tek: {tek}  Çift: {cift}  10. hane: {hane10}  11. hane: {hane11}  →  GEÇERLİ")
    else:
        print("→  GEÇERSİZ")
