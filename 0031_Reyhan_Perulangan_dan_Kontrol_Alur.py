# Menampilkan bilangan ganjil dan genap dari 1 sampai 50

print("Bilangan Genap:")

for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")

print("\n\nBilangan Ganjil:")

for i in range(1, 51):
    if i % 2 != 0:
        print(i, end=" ")

# Menampilkan bilangan prima dari 1 sampai 100

print("Bilangan prima 1-100:")

for angka in range(2, 101):
    prima = True

    for pembagi in range(2, angka):
        if angka % pembagi == 0:
            prima = False
            break

    if prima:
        print(angka, end=" ")