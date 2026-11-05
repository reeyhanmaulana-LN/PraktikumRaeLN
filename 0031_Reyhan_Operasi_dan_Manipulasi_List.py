print("soal 1.")
kendaraan = ['motor', 'mobil', 'sepeda', 'bus']

# a. Tambahkan 'truk' di akhir list
kendaraan.append('truk')
print("a. tambahkan truk :", kendaraan)

# b. Sisipkan 'becak' pada index ke-1
kendaraan.insert(1, 'becak')
print("b. sisipkan becak pada index 1 :", kendaraan)

# c. Hapus data yang berada paling belakang
kendaraan.pop()
print("c. hapus data paling belakang", kendaraan)

# d. Ubah elemen 'sepeda' menjadi 'skuter'
idx = kendaraan.index('sepeda')
kendaraan[idx] = 'skuter'
print("d. ubah sepeda menjadi skuter :", kendaraan)

# e. Tampilkan informasi jumlah total data
print(f"e. jumlah total data list: {len(kendaraan)}")

print("soal 2.")
angka = [75, 80, 90, 75, 85, 100, 65]

# a. Cari indeks skor 100
print("a. Skor 100 ada di indeks: {angka.index(100)}")

# b. Hitung banyak siswa skor 75
print("b. Jumlah skor 75: {angka.count(75)}")

# c. Urutkan list terkecil hingga terbesar
angka.sort()
print("c. List setelah diurutkan: {angka}")

# d. Balikkan urutan terbesar ke terkecil
angka.reverse()
print("d. List dari terbesar ke terkecil: {angka}")

print("soal 3.")
menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]

menu_utama.extend(menu_tambahan)
print(f"Daftar menu gabungan: {menu_utama}")

print("soal 4.")
data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]

# a. Menampilkan harga Pensil secara spesifik
print("a. menampilkan harga pensil", data_barang[1][1])

# b. Menampilkan output menggunakan perulangan
for barang in data_barang:
    print("b. menampilkan output menggunakan perulangan", f"Nama: {barang[0]}, Harga: {barang[1]}")