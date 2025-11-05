import numpy as np

nilai_ujian = np.array([
    82, 75, 90, 88, 70, 65, 95, 100, 85, 78,
    68, 92, 80, 73, 86, 91, 79, 83, 76, 98,
    71, 89, 81, 74, 93, 84, 77, 69, 96, 87
])


print("Nilai ujian dalam tipe data asli:", nilai_ujian)

nilai_sort = np.sort(nilai_ujian)[::-1]

print("Nilai ujian dalam tipe data short dan urutan terbalik:", nilai_short)