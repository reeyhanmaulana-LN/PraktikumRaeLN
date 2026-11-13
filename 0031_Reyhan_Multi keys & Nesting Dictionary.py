import datetime
import os
import string
import random

buku_template = {
    'judul': 'judul',
    'penulis': 'penulis',
    'tahun': 0,
    'terakhir_pinjam': datetime.datetime(1111, 1, 11),
    'status': False
}

data_perpustakaan = {}

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{'SISTEM MANAJEMEN PERPUSTAKAAN':^60}")
    print("-" * 60)

    buku = dict.fromkeys(buku_template.keys())
    buku['judul'] = input("Judul Buku: ")
    buku['penulis'] = input("Penulis Buku: ")
    buku['tahun'] = int(input("Tahun Terbit: "))

    TAHUN = int(input("Tahun Terakhir Pinjam (YYYY): "))
    BULAN = int(input("Bulan Terakhir Pinjam (1-12): "))
    TANGGAL = int(input("Tanggal Terakhir Pinjam (1-31): "))
    buku['terakhir_pinjam'] = datetime.datetime(TAHUN, BULAN, TANGGAL)

    status_input = input("Apakah buku tersedia? (y/n): ")
    buku['status'] = True if status_input.lower() == 'y' else False

    # Membuat key acak 6 karakter
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_perpustakaan.update({KEY: buku})

    print(f"\n{'KEYS':<8} {'JUDUL BUKU':<20} {'PENULIS':<15} {'TAHUN':<6} {'TANGGAL TERAKHIR PINJAM':<25} {'STATUS'}")
    print("-" * 90)

    for k in data_perpustakaan:
        JUDUL = data_perpustakaan[k]['judul']
        PENULIS = data_perpustakaan[k]['penulis']
        TAHUN_TERBIT = data_perpustakaan[k]['tahun']
        TGL_PINJAM = data_perpustakaan[k]['terakhir_pinjam'].strftime("%Y-%m-%d")
        STATUS = "TERSEDIA" if data_perpustakaan[k]['status'] else "TIDAK"
        
        print(f"{k:<8} {JUDUL:<20} {PENULIS:<15} {TAHUN_TERBIT:<6} {TGL_PINJAM:<25} {STATUS}")
    
    is_done = input("\nTambahkan buku baru lagi? (y/n): ")
    if is_done.lower() == 'n':
        break

print("\nAkhir dari program, terima kasih")