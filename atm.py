print("*****************************ATM*****************************")

bakiye=1000

kullanici_adi="YEK"
sifre="yek"
giris_hak=3

while True:
    kadi = input("Kullanıcı Adı Giriniz ")
    s = input("Şifre Giriniz ")

    if (kullanici_adi != kadi and sifre == s):
        print("Kullanici adınız yanlış")
        giris_hak -= 1
    elif (kullanici_adi == kadi and sifre != s):
        print("sifreniz yanlış")
        giris_hak -= 1
    elif (kullanici_adi != kadi and sifre != s):
        print("hepsi yanlıs dogru gir")
        giris_hak -= 1


    else:
        while True:

            islem = input("İşlem Gir( Çıkış Yapmak İçin q bas)")

            if (islem == "q"):
                print("Görüşmek Üzere")
                break
            elif (islem == "1"):
                print("Bakiyeniz", bakiye)
            elif (islem == "2"):
                yatir = int(input("Yatırılacak Miktarı Giriniz"))
                bakiye = bakiye + yatir
                print("yeni bakiye ", bakiye)
            elif (islem == "3"):
                cek = int(input("Çekilecek Miktarı Giriniz"))
                if bakiye - cek < 0 and cek % 10 == 0:
                    print("böyle bir miktar cekemezsin")
                    continue
                bakiye = bakiye - cek
                print("yeni bakiye ", bakiye)
            else:
                print("İslem Numaranızı Kontrol Ediniz")


    if (giris_hak == 0):
        print("kitlendi")
        break
