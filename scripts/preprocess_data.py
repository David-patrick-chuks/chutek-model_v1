import os
import pdfplumber
from docx import Document
from bs4 import BeautifulSoup

# Directories
RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"

# Helper: Extract text from PDF
def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        return "\n".join([page.extract_text() for page in pdf.pages])

# Helper: Extract text from DOCX
def extract_text_from_docx(file_path):
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

# Helper: Extract text from HTML
def extract_text_from_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        return soup.get_text()

# Process raw files
def process_raw_files():
    if not os.path.exists(PROCESSED_DIR):
        os.makedirs(PROCESSED_DIR)

    # Process each file in the raw data directory
    for file_name in os.listdir(RAW_DIR):
        file_path = os.path.join(RAW_DIR, file_name)
        text = ""

        if file_name.endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        elif file_name.endswith(".docx"):
            text = extract_text_from_docx(file_path)
        elif file_name.endswith(".html"):
            text = extract_text_from_html(file_path)
        else:
            print(f"Unsupported file type: {file_name}")
            continue

        # Save the processed text to a new file
        output_file = os.path.join(PROCESSED_DIR, f"{os.path.splitext(file_name)[0]}.txt")
        with open(output_file, "w", encoding="utf-8") as out_file:
            out_file.write(text)
        print(f"Processed {file_name} -> {output_file}")

# Merge all processed files into train_data.txt
def merge_processed_files():
    with open(os.path.join(PROCESSED_DIR, "train_data.txt"), "w", encoding="utf-8") as train_file:
        for file_name in os.listdir(PROCESSED_DIR):
            if file_name.endswith(".txt") and file_name != "train_data.txt":
                file_path = os.path.join(PROCESSED_DIR, file_name)
                with open(file_path, "r", encoding="utf-8") as f:
                    train_file.write(f.read() + "\n")
    print("Merged all processed files into train_data.txt")

# Main execution
if __name__ == "__main__":
    print("Starting preprocessing...")
    process_raw_files()
    merge_processed_files()
    print("Preprocessing completed!")
