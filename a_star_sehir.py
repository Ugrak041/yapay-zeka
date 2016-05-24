graph =  {'Canakkale': {'Izmir': 325 , 'Balikesir': 207 , 'Bursa': 271 , 'Tekirdag': 188 , 'Edirne': 217},
          'Izmir': {'Manisa': 36 , 'Usak': 211 , 'Canakkale': 325},
          'Balikesir': {'Manisa': 137 , 'Bursa': 151 , 'Canakkale': 207},
          'Edirne': {'Tekirdag': 140 , 'Istanbul': 229 , 'Canakkale': 217},
          'Manisa': {'Izmir': 36 , 'Balikesir': 137},
          'Bursa': {'Istanbul': 243 , 'Kocaeli': 132 , 'Eskisehir': 149 , 'Balikesir': 151, 'Canakkale': 271},
          'Tekirdag': {'Istanbul': 132 , 'Canakkale': 188 , 'Edirne': 140},
          'Usak': {'Afyon': 116 , 'Izmir': 211},
          'Istanbul': {'Kocaeli': 111 , 'Edirne': 229 , 'Bursa': 243 , 'Tekirdag': 132},
          'Kocaeli': {'Eskisehir': 219 , 'Bolu': 151 , 'Istanbul': 111 , 'Bursa': 132},
          'Eskisehir': {'Kutahya': 78 , 'Ankara': 233 , 'Kocaeli': 219 , 'Bursa': 149},
          'Bolu': {'Ankara': 191 , 'Kocaeli': 151},
          'Kutahya': {'Afyon': 100 , 'Eskisehir': 78},
          'Afyon': {'Ankara': 256 , 'Usak': 116},
          'Ankara': {'Eskisehir': 233 , 'Bolu': 191 , 'Afyon': 256}}

ankaraya_uzakliklar = {
    "Afyon": 239,
    "Ankara": 0,
    "Balikesir": 427,
    "Bolu": 139,
    "Bursa": 323,
    "Canakkale": 547,
    "Edirne": 565,
    "Eskisehir": 199,
    "Istanbul": 350,
    "Izmir": 521,
    "Kocaeli": 265,
    "Kutahya": 253,
    "Manisa": 490,
    "Tekirdag": 468,
    "Usak": 328
}

baslangic_sehri = 'Canakkale'
guzergah = [baslangic_sehri]
toplam_yol = 0

print("Baslangic sehri " + baslangic_sehri)

while guzergah[-1] != 'Ankara':
    simdiki_sehir = guzergah[-1]

    secilen_maliyet = -1
    secilen_komsu = ""

    for komsu in graph[simdiki_sehir]:
        if komsu in guzergah:
            print("  --  " + komsu + " sehri daha once ziyaret edildiginden atliyoruz.")
            continue
            # Bu sehire daha once geldiysek tekrar gitme.

        komsuya_uzaklik = graph[simdiki_sehir][komsu]
        ankaraya_uzaklik = ankaraya_uzakliklar[komsu]

        maliyet = komsuya_uzaklik + ankaraya_uzaklik
        print("  --  " + komsu + ", Uzaklik: " + str(komsuya_uzaklik) + ", Hedefe uzaklik: " + str(ankaraya_uzaklik) + ", Toplam Maliyet: " + str(maliyet))

        if secilen_maliyet == -1 or maliyet < secilen_maliyet:
            secilen_komsu = komsu
            secilen_maliyet = maliyet

    if secilen_komsu == "":
        print("")
        print("Ziyaret edilebilecek baska komsu kalmadi.")
        break

    print(secilen_komsu + " sehrine gidiliyor. Maliyet: " + str(secilen_maliyet) + " km")
    guzergah.append(secilen_komsu)
    toplam_yol = toplam_yol + komsuya_uzaklik
print("")
print("Guzergah: " + " -> ".join(guzergah))
print("Toplam katedilen yol: " + str(toplam_yol) + "km")

