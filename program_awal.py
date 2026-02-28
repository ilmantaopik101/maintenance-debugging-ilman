def hitung_rata_rata(nilai):
 total = 0
 for n in nilai:
 total = n
 return total / len(nilai)
def kategori_nilai(rata):
 if rata >= 85:
 return "A"
 elif rata >= 75:
 return "B"
 elif rata >= 65:
 return "C"
 else:
 return "D"
data = [80, 90, 75]
rata = hitung_rata_rata(data)
print("Rata-rata:", rata)
print("Kategori:", kategori_nilai)