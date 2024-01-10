import pandas as pd
from fpdf import FPDF
import chardet

def generate_pdf(input_csv, output_pdf):
    # Deteksi encoding file CSV
    with open(input_csv, 'rb') as file:
        result = chardet.detect(file.read())
    encoding = result['encoding']

    # Baca file CSV dengan encoding yang terdeteksi
    df = pd.read_csv(input_csv, encoding=encoding)

    # Buat dokumen PDF
    pdf = FPDF()
    pdf.add_page()

    # Input judul ujian
    exam_title = input("Masukkan nama ujian ex: Ujian Biologi : ")
    
    # Input kelas, semester, dan tahun ajaran
    class_info = input("Masukkan kelas ex: X IPA 1 : ")
    semester_info = input("Masukkan semester ex: Semester 1 : ")
    year_info = input("Masukkan tahun ajaran ex: 2023/2024 : ")

    # Header
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt=exam_title, ln=True, align='C')

    # Info kelas, semester, dan tahun ajaran (sebelah kiri)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, txt=f"Kelas: {class_info}", ln=True)
    pdf.cell(0, 10, txt=f"Semester: {semester_info}", ln=True)
    pdf.cell(0, 10, txt=f"Tahun Ajaran: {year_info}", ln=True)

    # Loop melalui setiap baris dalam file CSV
    for index, row in df.iterrows():
        question_number = index + 1
        question = f"{question_number}. {row['question']}"

        # Memisahkan jawaban palsu menjadi daftar
        all_answers = row['jawaban palsu'].split(',')

        # Tambahkan soal ke elemen PDF
        pdf.set_font("Arial", size=12)
        pdf.ln(10)
        pdf.multi_cell(0, 10, txt=question)

        # Tambahkan jawaban ke elemen PDF dengan format a., b., c., d.
        for idx, answer in enumerate(sorted(all_answers)):
            pdf.cell(0, 10, txt=f"{chr(97 + idx)}. {answer}", ln=True)

    # Simpan dokumen PDF
    pdf.output(output_pdf)

if __name__ == "__main__":
    input_csv = "generated_question.csv"
    output_pdf = "soal.pdf"
    generate_pdf(input_csv, output_pdf)
