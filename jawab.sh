#!/bin/bash

# Menentukan jumlah soal yang diinginkan
jumlah_soal=3

# Menjalankan soal.py untuk menghasilkan pertanyaan
for ((i=1; i<=$jumlah_soal; i++))
#do
 # python3 soal.py
#done

# Menjalankan jawaban.py untuk menghasilkan jawaban berdasarkan pertanyaan yang dihasilkan
python3 jawaban.py
