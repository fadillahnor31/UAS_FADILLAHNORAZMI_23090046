def main():
    data_mahasiswa = []

    while True:
        # Masukkan data mahasiswa
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        
        # Simpan data ke dalam daftar
        data_mahasiswa.append({'NIM': nim, 'Nama': nama})
        
        # Tanyakan apakah ingin menambah data lagi
        tambah_lagi = input("Ingin tambah lagi? (ya/tidak): ").strip().lower()
        if tambah_lagi != 'ya':
            break

    # Tampilkan data mahasiswa
    print("\nData Mahasiswa:")
    for mahasiswa in data_mahasiswa:
        print(f"NIM: {mahasiswa['NIM']}, Nama: {mahasiswa['Nama']}")

main()