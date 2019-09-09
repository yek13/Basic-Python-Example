
def tamBol(a):
    liste = list()
    for i in range(2,a):
        if a%i==0:
            liste.append(i)
    return liste

sayi=int(input("sayi gir"))
print(tamBol(sayi))