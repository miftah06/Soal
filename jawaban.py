import subprocess
import importlib
import pandas as pd
import numpy as np
import urllib3
import random
import os

def is_question_text(text):
    return not text.startswith('http') and ('exam' in text.lower() or 'finaltest' in text.lower() or 'search' in text.lower())

def install_package(package_name):
    try:
        importlib.import_module(package_name)
    except ImportError:
        subprocess.check_call(['pip3', 'install', package_name])

install_package('pandas')
install_package('numpy')
install_package('urllib3')

def generate_random_question(query, google_api_key, custom_search_engine_id, output_file='generated_question.csv', num_results=5):
    # Commented out Google Search API functionality
    # search_results = google_search(query, google_api_key, cx=custom_search_engine_id, num_results=num_results)
    
    # urls = [result['link'] for result in search_results]
    
    # if not urls:
    #     print("No search results found. Please try another query.")
    #     return None
    
    # chosen_url = random.choice(urls)
    # text_from_url = get_text_from_url(chosen_url)
    
    # while not is_question_text(text_from_url):
    #     chosen_url = random.choice(urls)
    #     text_from_url = get_text_from_url(chosen_url)
    
    # Use a different query for the question
    new_query = input("Masukkan soal atau pertanyaan anda: ")
    
    # Check if the file exists
    if os.path.exists(output_file):
        df_existing = pd.read_csv(output_file)
        answers_existing = df_existing['jawaban palsu'].tolist()
    else:
        answers_existing = []

    correct_answer = query
    
    question_number = len(answers_existing) + 1
    question = f"{new_query}"
    
    # Load answers from hasil.txt
    answers_from_file = get_answers_from_file('generated_katakunci.csv')
    
    sample_size = min(3, len(answers_from_file))
    choices = random.sample(answers_from_file, k=sample_size)
    
    choices.append(correct_answer)
    random.shuffle(choices)
    
    data = {'link': [''], 'question': [question], 'jawaban asli': [correct_answer], 'jawaban palsu': [', '.join(choices)]}
    df = pd.DataFrame(data)
    
    # Append the new question to the existing CSV file
    if os.path.exists(output_file):
        df.to_csv(output_file, mode='a', header=False, index=False)
    else:
        df.to_csv(output_file, index=False)

    return df

def get_text_from_url(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    return response.data.decode('utf-8')

def get_answers_from_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            answers = file.readlines()
        return [answer.strip() for answer in answers]
    return []

# Menentukan nama file untuk hasil pertanyaan dan jawaban
output_file = 'generated_question.csv'

# Continuous generation of questions
while True:
    query_to_search = input("Masukkan 1 jawaban benar anda: ")
    # Commented out Google API Key and Custom Search Engine ID
    # google_api_key = 'AIzaSyB7Mc1DkDq5HFlmh4RAa36TqJOXlhya-Q0'
    # custom_search_engine_id = '2285ae3ee0de64e4f'
    generated_question = generate_random_question(query_to_search, google_api_key='', custom_search_engine_id='')

    if generated_question is not None:
        print(f"Pertanyaan dan pilihan jawaban telah ditambahkan ke dalam {output_file}")
