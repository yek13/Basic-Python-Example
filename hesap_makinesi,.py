a=int(input("1.sayı gir"))
b=int(input("2.Sayi Gir"))

sonuc=int(input("İşlem"))

if (sonuc==1):
    print("{}+{}={}".format(a,b,a+b))
elif (sonuc==2):
    print("{}-{}={}".format(a,b,a-b))
elif (sonuc==3):
    print("{}*{}={}".format(a,b,a*b))
elif (sonuc==4):
    print("{}/{}={}".format(a,b,a/b))

else:
    print("düzgün sayı gir")