import os
from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    if len(text) > 1024:
        text = text[:1024]
    summary = summarizer(text, max_length=200, min_length=90, do_sample=False)
    return summary[0]['summary_text']

directory = "/Users/apple/ml-setup/ML/NLP work1/txt files" #directory path

documents = []
file_names = []

for file in os.listdir(directory):
    if file.endswith('.txt'):
        file_path = os.path.join(directory, file)
        with open(file_path, 'r', encoding='utf-8') as pp:
            data = pp.read() 
        
        documents.append(data)
        file_names.append(file)

vectorizer = TfidfVectorizer(max_df=0.85, stop_words='english')
matrix = vectorizer.fit_transform(documents)
feature_names = vectorizer.get_feature_names_out()


for i, document in enumerate(documents):
    summary = summarize_text(document)
    
    file_number = i + 1
    print(f'\n{"-"*10} Summary of file{file_number} {file_names[i]} {"-"*10}\n{summary}\n')
    
    doc_vector = matrix[i]
    sorted_items = doc_vector.toarray().flatten().argsort()[::-1]
    
    top_keywords = [feature_names[index] for index in sorted_items[:20]]
    
    print(f"{'-'*10}Top keywords for file{file_number} {file_names[i]}{'-'*10}")
    print(", ".join(top_keywords))
    print("\n")
