sekil=input("İstediğiniz Şekli gir")

if sekil=="Dörtgen":
    k1=input("1 kenar gir")
    k2=input("2. kenar gir")
    k3=input("3. kenar gir" )
    k4=input("4. kenar gir ")

    if k1==k2 and k2==k3 and k3==k4:
        print("Kare")
    elif k1==k2 and k3==k4:
        print("dikdörtgen")
    else:
        print("dörtgen")

elif sekil=="Üçgen":
    a = int(input("Kenar-1:"))
    b = int(input("Kenar-2:"))
    c = int(input("Kenar-3:"))

    if abs(a+b)>c and abs(a+c)>b and abs(b+c)>a:
        if a==b and a==c:
            print("Eşkenar Üçgen")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("İkizkenar Üçgen....")
        else:
            print("Çeşitkenar")
    else:
        print("üçgen değil")
else:
    print("gecersiz şekil")