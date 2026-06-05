'''
====================================================================
PROYEK AKHIR BAHASA PEMROGRAMAN (CIE201)
Nama Proyek: Sistem Aplikasi Kasir & Katalog Merchandise Chindoren
Versi      : 1.0 (CLI Based)
Deskripsi   : Aplikasi kasir sederhana untuk mengelola penjualan merchandise Chindoren,
              termasuk katalog produk, keranjang belanja, dan proses checkout dengan diskon 
              otomatis.
====================================================================

'''

katalog_produk = {
    "1": {"nama": "Hoodie Gamer Chindoren", "harga": 150000, "stok": 10},
    "2": {"nama": "Topi Elegan Chindoren", "harga": 75000, "stok": 15},
    "3": {"nama": "Kaos Katun Premium", "harga": 110000, "stok": 8},
    "4": {"nama": "Gantungan Kunci Akrilik", "harga": 15000, "stok": 50}
}

keranjang_belanja = []

def tampilkan_katalog():
    """Tampilkan daftar produk beserta harga dan stok."""
    print("\n========================================")
    print("         KATALOG MERCHANDISE CHINDOREN   ")
    print("========================================")
    for kode, info in katalog_produk.items():
        print(f"[{kode}] {info['nama']}\n    Harga: Rp {info['harga']:,} | Stok tersedia: {info['stok']}")
    print("========================================")


def hitung_diskon(total_belanja):
    """Hitung diskon sesuai total belanja."""
    if total_belanja >= 250000:
        return total_belanja * 0.10
    elif total_belanja >= 100000:
        return total_belanja * 0.05
    return 0


while True:
    print("\n--- SISTEM KASIR KELOMPOK CHINDOREN ---")
    print("1. Tampilkan Katalog Produk")
    print("2. Tambah Item ke Keranjang")
    print("3. Lihat Isi Keranjang")
    print("4. Proses Pembayaran (Checkout)")
    print("5. Keluar dari Aplikasi")

    pilihan_menu = input("Silakan pilih menu (1-5): ")

    if pilihan_menu == "1":
        tampilkan_katalog()

    elif pilihan_menu == "2":
        tampilkan_katalog()
        kode_barang = input("Masukkan KODE produk yang ingin dibeli: ")

        if kode_barang in katalog_produk:
            produk_terpilih = katalog_produk[kode_barang]

            if produk_terpilih["stok"] > 0:
                jumlah_beli = int(input(f"Berapa banyak {produk_terpilih['nama']} yang ingin dibeli? "))

                if jumlah_beli <= produk_terpilih["stok"]:
                    produk_terpilih["stok"] -= jumlah_beli
                    item_keranjang = {
                        "nama": produk_terpilih["nama"],
                        "harga": produk_terpilih["harga"],
                        "jumlah": jumlah_beli
                    }
                    keranjang_belanja.append(item_keranjang)
                    print(f"Berhasil menambahkan {jumlah_beli}x {produk_terpilih['nama']} ke keranjang.")
                else:
                    print("Transaksi Gagal: Jumlah beli melebihi batas stok aktif!")
            else:
                print("Transaksi Gagal: Stok barang ini sudah habis terjual!")
        else:
            print("Transaksi Gagal: Kode produk salah atau tidak terdaftar!")

    elif pilihan_menu == "3":
        print("\n--- ISI KERANJANG BELANJA SAAT INI ---")
        if not keranjang_belanja:
            print("[Keranjang Anda masih kosong. Silakan belanja terlebih dahulu]")
        else:
            nomor_urut = 1
            for item in keranjang_belanja:
                subtotal_item = item["harga"] * item["jumlah"]
                print(f"{nomor_urut}. {item['nama']} ({item['jumlah']} pcs) - Subtotal: Rp {subtotal_item:,}")
                nomor_urut += 1

    elif pilihan_menu == "4":
        if not keranjang_belanja:
            print("Transaksi Gagal: Tidak ada barang di dalam keranjang untuk diproses!")
            continue

        print("\n========================================")
        print("          NOTA PEMBAYARAN CHINDOREN       ")
        print("==========================================")

        total_harga_kotor = 0
        for item in keranjang_belanja:
            subtotal_item = item["harga"] * item["jumlah"]
            total_harga_kotor += subtotal_item
            print(f"• {item['nama']} x{item['jumlah']} = Rp {subtotal_item:,}")
            
        jumlah_potongan = hitung_diskon(total_harga_kotor)
        total_akhir_bersih = total_harga_kotor - jumlah_potongan

        print("----------------------------------------")
        print(f"Total Sebelum Diskon : Rp {total_harga_kotor:,}")
        print(f"Diskon Didapatkan    : Rp {jumlah_potongan:,}")
        print(f"TOTAL YANG HARUS BAYAR: Rp {total_akhir_bersih:,}")
        print("========================================")

        keranjang_belanja.clear()
        print("Pembayaran Selesai! Struk berhasil dicetak dan keranjang dikosongkan.")

    elif pilihan_menu == "5":
        print("Keluar dari program... Terima kasih telah mengelola toko Chindoren hari ini!")
        break

    else:
        print("Transaksi Gagal: Pilihan salah! Harap masukkan angka menu antara 1 sampai 5.")