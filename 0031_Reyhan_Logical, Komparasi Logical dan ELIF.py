#Pertemuan_4 11 September 2026

# Program menentukan kategori usia

usia = int(input("Masukkan usia: "))

if usia > 0 and usia < 12:
    print("Kategori: Anak-anak")
elif usia > 13 and usia < 17:
    print("Kategori: Remaja")
elif usia > 18 and usia < 59:
    print("Kategori: Dewasa")
else:
    print("Kategori: Lansia")