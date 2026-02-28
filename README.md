# maintenance-debugging-Python_code

# BUG LOGIKA PENJUMLAHAN YANG SALAH

# 1) PENJELASAN BUG
Variabel total setiap kali ditimpa oleh nilai n, bukan dijumlahkan.
Artinya setelah loop selesai, total hanya berisi nilai terakhir dari list.

#potongan kode:
for n in nilai:
    total = n

Iterasi berjalan seperti ini:

total = 80
total = 90
total = 75

Hasil rata rata = 25
Padahal seharusnya 80 + 90 + 75 = 245 : 3 = 81.67

# 2) JENIS ERROR
Pada kasus ini memiliki logic error, karena syntax yang di tulis bisa berjalan namun hanya kesalahan penghitungannya.

# 3) SOLUSI
Ubah potongan kode berikut:
for n in nilai:
    total = n

menjadi:
for n in nilai:
    total += n


# FUNGSI TIDAK DIPANGGIL
Potongan kode:
print("Kategori:", kategori_nilai)

# 1) Penjelasan Bug

Di sini fungsi kategori_nilai tidak dipanggil.
Yang dicetak hanyalah objek fungsi itu sendiri.

Hasilnya akan menjadi seperti ini:
Kategori: <function kategori_nilai at 0x7be736d9c220>

# 2) Jenis Error

Logic Error
Bukan runtime error, karena tidak terjadi crash program berjalan, tapi maksudnya tidak tercapai.

Runtime error itu seperti membagi dengan nol atau mengakses index yang tidak ada. Program langsung berhenti.
jadi disini program tetap hidup, tapi salah makna.

# 3) Solusi

Panggil fungsi dengan parameter (rata):

print("Kategori:", kategori_nilai(rata))






# PERTANYAAN ANALISIS
1. Mengapa bug logika lebih berbahaya daripada syntax error?
2. Apa risiko jika debugging dilakukan tanpa pengujian ulang?
3. Bagaimana praktik version control membantu maintenance?

# 1. Mengapa bug logika lebih berbahaya daripada syntax error?

Program tetap berjalan,output tetap muncul,semua terlihat normal. Tapi hasilnya salah.
Bahaya utamanya ada pada ilusi kebenaran.
Sistem memberi rasa aman palsu.

Contoh kecil dari praktikum diatas:

* Program tidak crash.
* Output keluar.
* Tapi rata-rata salah.

# 2. Apa risiko jika debugging dilakukan tanpa pengujian ulang?

Tanpa pengujian ulang:
* Kita tidak tahu apakah bug benar-benar hilang.
* Bisa muncul bug baru (regression bug).
* Bisa saja perbaikan memperbaiki satu bagian tapi merusak bagian lain.
Debugging tanpa testing itu hanya asumsi.
Dalam rekayasa perangkat lunak, pengujian ulang berfungsi sebagai verifikasi yang jelas.

# 3. Bagaimana praktik version control membantu maintenance?

Version control seperti Git menyimpan sejarah evolusi kode.

Manfaatnya:

Pertama, kita bisa melihat perubahan apa yang menyebabkan bug muncul.
Kedua, kita bisa kembali ke versi stabil sebelumnya.
Ketiga, setiap perubahan terdokumentasi dengan jelas.
Keempat, kolaborasi menjadi terkendali, tidak ada yang menimpa pekerjaan orang lain secara sembarangan.

Dalam konteks maintenance, version control memberikan traceability — kemampuan menelusuri perubahan.
Tanpa version control, debugging itu seperti mencari kesalahan dalam dokumen tanpa tahu siapa yang terakhir mengedit dan apa yang diubah.
Dengan version control, membuat kita punya “jejak digital evolusi sistem”.
