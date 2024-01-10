Soal-Generator

Soal-Generator adalah skrip sederhana untuk menghasilkan soal acak berbasis teks. Skrip ini memungkinkan pengguna untuk membuat sejumlah soal pilihan ganda dengan variasi yang dapat dikonfigurasi.
Cara Menggunakan

    Pastikan Python sudah terinstal di sistem Anda. Jika belum, Anda dapat mengunduhnya dari python.org.

    Unduh proyek ini ke sistem Anda atau gunakan perintah git clone:

    bash

git clone https://github.com/miftah06/Soal.git

Masuk ke direktori proyek:

bash

cd Soal-Generator

Install dependensi yang dibutuhkan:

bash

pip install -r requirements.txt

Konfigurasi skrip sesuai kebutuhan Anda dengan mengedit file config.py.

Jalankan skrip dengan perintah:

bash

    python soal.py

    Soal akan dihasilkan dan disimpan dalam file soal.pdf.

Konfigurasi

Anda dapat mengonfigurasi berbagai aspek skrip melalui file config.py. Beberapa pengaturan yang dapat diubah termasuk jumlah soal yang akan dibuat, jenis pertanyaan, dan format penyimpanan file output.

python

# jawaban.py

# Jumlah soal yang akan dihasilkan
JUMLAH_SOAL = 10 atau tergantung soal yang di generate jawaban.py
ke generated_question.csv

# generator.py
fungsi dari generator.py adalah untuk meghasilkan generated_katakunci.csv yang akan menjadi
berupa jawaban - jawaban palsu untuk soal pertanyaan kita

# hasilkan.py
fungsi dari generator.py adalah untuk meghasilkan hasil.txt yang akan menjadi
bahan untuk di olah generator.py 
berupa txt yang berisi data 
yang bisa kalian masukkan untuk menjadi jawaban soal kita
ke katakunci.txt jangan lupa isi keyword.txt untuk menghasilkan 
jika kebingungan ada keyword planner jika masih bingung bisa
lansung ke generator.py saja

# Format penyimpanan file output
FORMAT_OUTPUT = "pdf"

Kontribusi

Jika Anda ingin berkontribusi pada proyek ini, silakan buat fork dari repositori ini, lakukan perubahan Anda, dan ajukan pull request. Kami sangat menghargai kontribusi dari komunitas.
Catatan

Proyek ini masih dalam pengembangan aktif, dan umpan balik dari pengguna sangat dihargai. Silakan buat issue untuk melaporkan bug atau saran perbaikan.

Terima kasih telah menggunakan Soal-Generator! Semoga bermanfaat.