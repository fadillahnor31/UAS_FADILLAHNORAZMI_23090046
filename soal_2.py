data = [
    ["Nama", "Mahasiswa 1", "Mahasiswa 2", "Mahasiswa 3"],
    ["Algoritma dan Struktur Data 2", 90, 75, 65],
    ["Matematika Numerik", 80, 70, 75]
]
def rata_rata_matakuliah(data):
    rata_rata = {}
    for i in range(1, len(data)):
        matakuliah = data[i][0]
        nilai = data[i][1:]
        rata_rata[matakuliah] = sum(nilai) / len(nilai)
    return rata_rata

# Menghitung rata-rata nilai setiap mahasiswa
def rata_rata_mahasiswa(data):
    rata_rata = {}
    for j in range(1, len(data[0])):
        nama_mahasiswa = data[0][j]
        nilai_mahasiswa = [data[i][j] for i in range(1, len(data))]
        rata_rata[nama_mahasiswa] = sum(nilai_mahasiswa) / len(nilai_mahasiswa)
    return rata_rata


rata_rata_matkul = rata_rata_matakuliah(data)
print("Rata-rata nilai untuk setiap mata kuliah:")
for matakuliah, rata2 in rata_rata_matkul.items():
    print(f"{matakuliah}: {rata2}")


rata_rata_mhs = rata_rata_mahasiswa(data)
print("\nRata-rata nilai untuk setiap mahasiswa:")
for mahasiswa, rata2 in rata_rata_mhs.items():
    print(f"{mahasiswa}: {rata2}")