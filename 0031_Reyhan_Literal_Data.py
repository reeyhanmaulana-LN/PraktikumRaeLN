#Pertemuan_2 28 Agustus 2026

#Soal 1
print("1. Membuat Variabel Sesuai Tipe Data")
nama = "Reyhan Maulana A.M"
umur = 18
berat = 75.0

print("Nama :", nama)
print("Umur :", umur)
print("Berat :", berat)

input("\nTekan Enter untuk melanjutkan soal no 2")

#Soal 2
print("2. Konversi Tipe Data")
angka_string = "123" #angka menggunakan tanda kutip ("") dianggap sebagai huruf/simbol biasa bukan angka yang bisa ditambah atau dikurangi
angka_float = 45.67 #bilangan desimal atau pecahan
angka_integer = 89 #bilangan bulat

# Konversi string menjadi integer
string_ke_integer = int(angka_string)
# Konversi float menjadi integer
float_ke_integer = int(angka_float)
# Konversi integer menjadi float
integer_ke_float = int(angka_integer)
# Konversi integer menjadi string
integer_ke_string = int(angka_integer)

print("String ke Integer =", string_ke_integer)
print("Float ke Integer =", float_ke_integer)
print("Integer ke Float =", integer_ke_float)
print("Integer ke String =", integer_ke_string)

input("\nTekan Enter untuk soal no 3")

#Soal 3
nama = input("Nama : ")
usia = int(input("Usia : "))
tinggi = float(input("Tinggi Badan :"))

print("\n--- DATA DIRI ---")
print("Nama :", nama)
print("Usia :", usia)
print("Tinggi :", tinggi, "cm")

print("\n Terimakasih Sudah Mengisi")