print("***********FAKTORİYEL************")

while True:

    sayi=input("sayi giriniz")
    if(sayi=="q"):
        break
    sayi=int(sayi)
    fakt=1
    for i in range(2,sayi+1):

        fakt=fakt*i

    print(fakt)
