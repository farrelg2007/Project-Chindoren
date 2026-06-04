# ====================================================================
# PROYEK AKHIR BAHASA PEMROGRAMAN (CIE201)
# Nama Proyek: Sistem Aplikasi Kasir & Katalog Merchandise Chindoren
# Versi      : 1.0 (Fase UTS - CLI Base)
# ====================================================================

# === SESI 7: DICTIONARY & SET (Pengelolaan Key-Value & Data Unik) ===
# Menyimpan database produk lokal secara terstruktur
katalog_produk = {
    "1": {"nama": "Hoodie Gamer Chindoren", "harga": 150000, "stok": 10},
    "2": {"nama": "Topi Elegan Chindoren", "harga": 75000, "stok": 15},
    "3": {"nama": "Kaos Katun Premium", "harga": 110000, "stok": 8},
    "4": {"nama": "Gantungan Kunci Akrilik", "harga": 15000, "stok": 50}
}

# === SESI 5: LIST (Penyimpanan Sementara Data Kelompok) ===
# List ini digunakan untuk menampung item yang dimasukkan ke keranjang
keranjang_belanja = []


# === SESI 6: MODULARISASI KODE (Penggunaan Fungsi/Function) ===
def tampilkan_katalog():
    """Fungsi non-parameter untuk menampilkan daftar barang"""
    print("\n========================================")
    print("         KATALOG MERCHANDISE CHINDOREN   ")
    print("========================================")
    # Perulangan untuk membaca Dictionary (Sesi 4 & Sesi 7)
    for kode, info in katalog_produk.items():
        print(f"[{kode}] {info['nama']}\n    Harga: Rp {info['harga']:,} | Stok tersedia: {info['stok']}")
    print("========================================")


def hitung_diskon(total_belanja):
    """Fungsi dengan parameter dan return value untuk aturan keputusan"""
    # === SESI 3: ATURAN KEPUTUSAN (Percabangan If-Elif-Else) ===
    if total_belanja >= 250000:
        return total_belanja * 0.10  # Diskon 10% jika belanja >= 250 ribu
    elif total_belanja >= 100000:
        return total_belanja * 0.05  # Diskon 5% jika belanja >= 100 ribu
    else:
        return 0  # Tidak dapat diskon


# === SESI 4: MEKANISME PENGULANGAN (While Loop Menu Utama) ===
# Menggunakan Loop tak terbatas agar program tidak langsung mati sebelum kasir keluar
while True:
    print("\n--- SISTEM KASIR KELOMPOK CHINDOREN ---")
    print("1. Tampilkan Katalog Produk")
    print("2. Tambah Item ke Keranjang")
    print("3. Lihat Isi Keranjang")
    print("4. Proses Pembayaran (Checkout)")
    print("5. Keluar dari Aplikasi")
    
    # === SESI 1: INPUT-PROCESS-OUTPUT (IPO BARIS DASAR) ===
    pilihan_menu = input("Silakan pilih menu (1-5): ")

    # Sesi 3: Percabangan Menu Utama
    if pilihan_menu == "1":
        tampilkan_katalog()
        
    elif pilihan_menu == "2":
        tampilkan_katalog()
        kode_barang = input("Masukkan KODE produk yang ingin dibeli: ")
        
        # Sesi 3: Validasi apakah kode barang ada di Dictionary katalog
        if kode_barang in katalog_produk:
            produk_terpilih = katalog_produk[kode_barang]
            
            if produk_terpilih["stok"] > 0:
                # Sesi 1 & 2: Input kuantitas dan konversi tipe data (Casting ke Integer)
                jumlah_beli = int(input(f"Berapa banyak {produk_terpilih['nama']} yang ingin dibeli? "))
                
                # Sesi 3: Validasi kecukupan stok barang
                if jumlah_beli <= produk_terpilih["stok"]:
                    # === SESI 2: VARIABEL & OPERASI ARITMATIKA ===
                    # Mengurangi stok di katalog utama
                    produk_terpilih["stok"] -= jumlah_beli
                    
                    # Memasukkan data baru berbentuk dictionary ke dalam List Keranjang (Sesi 5)
                    item_keranjang = {
                        "nama": produk_terpilih["nama"],
                        "harga": produk_terpilih["harga"],
                        "jumlah": jumlah_beli
                    }
                    keranjang_belanja.append(item_keranjang)
                    print(f"✓ Berhasil menambahkan {jumlah_beli}x {produk_terpilih['nama']} ke keranjang.")
                else:
                    print("⚠ Transaksi Gagal: Jumlah beli melebihi batas stok aktif!")
            else:
                print("⚠ Transaksi Gagal: Stok barang ini sudah habis terjual!")
        else:
            print("⚠ Transaksi Gagal: Kode produk salah atau tidak terdaftar!")

    elif pilihan_menu == "3":
        print("\n--- ISI KERANJANG BELANJA SAAT INI ---")
        # Sesi 3: Memeriksa apakah list keranjang kosong
        if not keranjang_belanja:
            print("[Keranjang Anda masih kosong. Silakan belanja terlebih dahulu]")
        else:
            # Sesi 4 & 5: Iterasi membaca elemen di dalam List
            nomor_urut = 1
            for item in keranjang_belanja:
                # Sesi 2: Perhitungan subtotal per item (Harga dikali Jumlah)
                subtotal_item = item["harga"] * item["jumlah"]
                print(f"{nomor_urut}. {item['nama']} ({item['jumlah']} pcs) - Subtotal: Rp {subtotal_item:,}")
                nomor_urut += 1

    elif pilihan_menu == "4":
        if not keranjang_belanja:
            print("⚠ Checkout Gagal: Tidak ada barang di dalam keranjang untuk diproses!")
            continue # Melompati sisa kode di loop bawah dan kembali ke menu utama
            
        print("\n========================================")
        print("          NOTA PEMBAYARAN CHINDOREN       ")
        print("==========================================")
        
        total_harga_kotor = 0
        for item in keranjang_belanja:
            subtotal_item = item["harga"] * item["jumlah"]
            # Sesi 2: Operator Penugasan Akumulasi (+=)
            total_harga_kotor += subtotal_item
            print(f"• {item['nama']} x{item['jumlah']} = Rp {subtotal_item:,}")
            
        # Sesi 6: Memanggil fungsi perhitungan diskon dengan argumen total harga kotor
        jumlah_potongan = hitung_diskon(total_harga_kotor)
        total_akhir_bersih = total_harga_kotor - jumlah_potongan
        
        print("----------------------------------------")
        print(f"Total Sebelum Diskon : Rp {total_harga_kotor:,}")
        print(f"Diskon Didapatkan    : Rp {jumlah_potongan:,}")
        print(f"TOTAL YANG HARUS BAYAR: Rp {total_akhir_bersih:,}")
        print("========================================")
        
        # Sesi 5: Mengosongkan kembali isi List keranjang belanja setelah transaksi sukses
        keranjang_belanja.clear()
        print("✓ Pembayaran Selesai! Struk berhasil dicetak dan keranjang dikosongkan.")

    elif pilihan_menu == "5":
        print("\nKeluar dari program... Terima kasih telah mengelola toko Chindoren hari ini!")
        break # Sesi 4: Menghentikan paksa perulangan While True untuk menutup aplikasi
        
    else:
        print("⚠ Pilihan salah! Harap masukkan angka menu antara 1 sampai 5.")