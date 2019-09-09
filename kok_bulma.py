"""
a=int(input("a :"))

b=int(input("b :"))
c=int(input("c :"))



delta=b**2 -4*a*c
x1=(-b-delta**0.5)/(2*a)
x2=(-b+delta**0.5)/(2*a)

print("1.Kök :{} \n2.Kök:{}  ".format(x1,x2))
"""
a=float(input("boy :"))

b=int(input("kilo :"))

kitleendeksi=b/a**2

if kitleendeksi<18.5:
    print("zaayıf")
elif kitleendeksi in range(18,25):

    print("normal")
elif kitleendeksi > 25 and kitleendeksi < 30:

    print("fazla kilolu")
elif kitleendeksi > 30:

    print("obez")

else:
    print("Çldün Çık")
