import PyPDF2
import camelot

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = [page.extract_text() for page in reader.pages]
    return text

def extract_tables_from_pdf(file_path):
    tables = camelot.read_pdf(file_path, pages='all', flavor='stream')
    return [table.df for table in tables]
