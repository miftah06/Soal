import pandas as pd
import numpy as np
import random

def generate_object_names(keywords_file, num_objects=1000):
    # Membaca kata kunci dari file
    with open(keywords_file, 'r') as file:
        keywords = file.read().splitlines()

    # Memastikan jumlah kata kunci cukup untuk menghasilkan objek
    if len(keywords) < 5:
        raise ValueError("Jumlah kata kunci harus minimal 5 untuk menghasilkan objek.")

    # Menghasilkan nama objek secara acak
    object_names = []
    for _ in range(num_objects):
        object_name = f"{random.choice(keywords)} {random.choice(keywords)}"
        object_names.append(object_name)

    # Membuat DataFrame dengan nama objek
    data = {'Nama Objek Jawaban': object_names}
    df = pd.DataFrame(data)

    return df

# Contoh penggunaan
keywords_file = 'katakunci.txt'  # Ganti dengan file yang berisi kata kunci
num_objects_to_generate = 1000  # Ganti dengan jumlah objek yang ingin dihasilkan
generated_objects = generate_object_names(keywords_file, num_objects_to_generate)

# Menyimpan DataFrame ke file CSV
generated_objects.to_csv('generated_katakunci.csv', index=False)

print(f"{num_objects_to_generate} Nama objek telah disimpan ke dalam generated_katakunci.csv")
