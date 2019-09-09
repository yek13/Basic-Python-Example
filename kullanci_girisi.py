print("********************************KULLANICI GİRİŞİ********************************")


kullanici_adi="YEK"
sifre="yek"
giris_hak=3
while True:
    kadi=input("Kullanıcı Adı Giriniz ")
    s=input("Şifre Giriniz ")
    if (kullanici_adi!=kadi and sifre==s):
        print("Kullanici adınız yanlış")
        giris_hak-=1
    elif (kullanici_adi==kadi and sifre!=s):
        print("sifreniz yanlış")
        giris_hak-=1
    elif (kullanici_adi != kadi and sifre != s):
        print("hepsi yanlıs dogru gir")
        giris_hak -= 1

    else:
        print("tebrikler")
        break

    if(giris_hak==0):
        print("kitlendi")
        break