"""
MÜKEMMEL SAYI

def mukemmel(a):
    toplam=0
    for i in range(1,a):


        if a%i==0:

            toplam+=i

    return toplam==a

while True:

    sayi=input("sayi giriniz")

    if (sayi=="q"):

        print("görüşürüz")
        break
    else:
        sayi=int(sayi)
        if mukemmel(sayi):
            print("{} Mükemmel".format(sayi))

        else:
            print("{} Mükemmel Değil".format(sayi))

-----
#1000 e kadar
for i in range(1,1001):
    if(mukemmel(i)):
        print("mükemmel sayınız  :",i)
-----------------------------------------------------------
EBOB SORUSU

def ebob(a,b):
    listea = list()
    listeb = list()
    ortak = list()

    for i in range(1,a):
        if a%i==0:

            listea.append(i)
    print("a değişkeninin tam bölenleri=",listea)


    for j in range(1,b):
        if b%j==0:

            listeb.append(j)
    print("a değişkeninin tam bölenleri=",listeb)

    for x in listea:
        for y in listeb:
            if x==y:
                ortak.append(x)
    print("ortak bölenler=",ortak)
    ebobunuz=max(ortak)

    return ("Ebobunuz {}'dır".format(ebobunuz))



a=int(input("a sayısını giriniz"))
b=int(input("b sayısını giriniz"))
print(ebob(a,b))

----------------------------------

EKOK SORUSU

def ekok (a,b):
    la=list()
    lb=list()
    o=list()

    for i in range(1,a):
        if a%i==0:
            la.append(i)
    print("a değişkeninin tam bölenleri=", la)

    for i in range(1,b):
        if b%i==0:
            lb.append(i)
    print("a değişkeninin tam bölenleri=", lb)
    for x in la:
        for y in lb:
            if x == y:
                o.append(x)
    print("ortak bölenler=", o)
    ekokunuz = min(o)

    return ("Ekokunuz {}'dır".format(ekokunuz))

ilksayi=int(input("a sayısını giriniz"))
ikincisayi=int(input("b sayısını giriniz"))
print(ekok(ilksayi,ikincisayi))

---------------
100'E KADAR PİSAGOR ÜCGENLERİ

def pisagor():
    pisagorr=list()
    for i in range(1,101):
        for j in range(1,101):
            hesap=((i**2)+(j**2))**0.5
            if (hesap == int(hesap) ):
                pisagorr.append((i,j,int(hesap)))
    return pisagorr

for i in pisagor():
    print(i)

"""