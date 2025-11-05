import numpy as np

keuntungan_harian = np.array([
    150, 175, 210, 180, 230, 190, 165,
    205, 220, 185, 195, 240, 170, 200
])

print(f"Data Keuntungan 14 Hari (dalam ribuan Rp):\n{keuntungan_harian}\n")

rata_rata_keuntungan = np.mean(keuntungan_harian)
print(f"Rata-rata Keuntungan Harian: {rata_rata_keuntungan:.2f} ribu Rp")

keuntungan_tertinggi = np.max(keuntungan_harian)
keuntungan_terendah = np.min(keuntungan_harian)

hari_terendah = np.argmin(keuntungan_harian) + 1

print(f"Keuntungan Tertinggi: {keuntungan_tertinggi} ribu Rp (Terjadi pada hari ke-{hari_tertinggi})")
print(f"Keuntungan Terendah : {keuntungan_terendah} ribu Rp (Terjadi pada hari ke-{hari_terendah})")