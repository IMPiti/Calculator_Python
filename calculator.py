def toplama(x, y):
    return x+y


def cikarma(x, y):
    return x-y


def carpma(x, y):
    return x*y


def bolme(x, y):
    return x/y


print()
print("##############")
print("HESAP MAKİNESİ")
print("##############")
print()
print(f" Toplama için : 1\n Çıkartma için : 2\n Çarpma için : 3\n Bölme için : 4'ü giriniz...")

print()


secim = input("Yapmak istediğiniz işlemi giriniz ")


sayi1 = int(input("İlk Sayıyı giriniz : "))
sayi2 = int(input("İkinci Sayıyı Giriniz : "))

if secim == "1":
    print(f"{sayi1} + {sayi2} = {toplama(sayi1, sayi2)}")
elif secim == "2":
    print(f"{sayi1} - {sayi2} = {cikarma(sayi1, sayi2)}")
elif secim == "3":
    print(f"{sayi1} * {sayi2} = {carpma(sayi1, sayi2)}")
elif secim == "4":
    print(f"{sayi1} / {sayi2} = {bolme(sayi1, sayi2)}")
else:
    print(f"Geçersiz bir komut girdiniz...")
