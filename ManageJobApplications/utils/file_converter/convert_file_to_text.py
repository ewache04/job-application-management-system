import os
import tempfile
import zipfile

import PyPDF2
import docx
import pypandoc
from bs4 import BeautifulSoup


def convert_pdf_to_text(file_path):
    text = """"""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text


def convert_docx_to_text(file_path):
    doc = docx.Document(file_path)
    full_text = []
    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)
    return '\n'.join(full_text)


def convert_rtf_to_text(file_path):
    output = pypandoc.convert_file(file_path, 'plain', format='rtf')
    return output


def convert_html_to_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        return soup.get_text()


def extract_and_convert_zip(zip_path):
    extracted_texts = []
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        with tempfile.TemporaryDirectory() as temp_dir:
            zip_ref.extractall(temp_dir)
            for root, _, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        extracted_texts.append(convert_file_to_text(file_path))
                    except ValueError:
                        # Skip unsupported files within the zip
                        continue
    return "\n".join(extracted_texts)


def convert_file_to_text(file_path):
    
    try:
        if file_path.endswith('.pdf'):
            return convert_pdf_to_text(file_path)
        elif file_path.endswith('.docx'):
            return convert_docx_to_text(file_path)
        elif file_path.endswith('.rtf'):
            return convert_rtf_to_text(file_path)
        elif file_path.endswith('.html'):
            return convert_html_to_text(file_path)
        elif file_path.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        elif file_path.endswith('.zip'):
            return extract_and_convert_zip(file_path)
        else:
            raise ValueError("Unsupported file format")
    except Exception as e:
        print(f"Conversion failed: {str(e)}")
        return None

# Example usage:
# if __name__ == "__main__":
#     text = convert_file_to_text(file_path)
#     print(text)
