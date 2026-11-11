print("Soal 1")
# a. Membuat Tuple data diri
mahasiswa = ("Reyhan Maulana A.M", "2605060031", "Teknologi Informasi")

# b. Menampilkan data NIM dan Prodi ke layar menggunakan indeks
print("NIM   :", mahasiswa[1])
print("Prodi :", mahasiswa[2])

# c. Penjelasan Error Tuple
# mahasiswa[2] = "Teknologi Informasi"
# Jika perintah di atas dijalankan, akan menghasilkan pesan error: 
# "TypeError: 'tuple' object does not support item assignment".
# Hal ini terjadi karena tuple bersifat Immutable (tidak dapat diubah setelah dideklarasikan)[cite: 1, 4].

# d. Membuat Set
nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print("Isi nilai_angka:", nilai_angka)

print("Soal 2")
# a. Membuat dictionary data_mahasiswa
data_mahasiswa = {
    "nim": "240101",
    "nama": "Budi Santoso",
    "prodi": "Teknologi Informasi"
}

# b. Mengubah nilai prodi dan menambahkan key baru
data_mahasiswa["prodi"] = "Sastra Mesin"
data_mahasiswa.update({"angkatan": 2026})

# c. Menghapus data nim dan mencetak ke layar
del data_mahasiswa["nim"]
print("Hasil akhir data mahasiswa:")
print(data_mahasiswa)

print("Soal 3")
# a. Membuat dictionary keranjang
keranjang = {
    "apel": 5000, 
    "pisang": 3000, 
    "jeruk": 7000, 
    "anggur": 15000
}

# b. Menampilkan setiap barang dan harga dengan perulangan
total_belanja = 0
for buah, harga in keranjang.items():
    print(f"Harga {buah}: Rp {harga}")
    total_belanja += harga

# c. Menampilkan total belanja
print(f"Total belanja: Rp {total_belanja}")