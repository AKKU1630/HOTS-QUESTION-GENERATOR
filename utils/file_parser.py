import fitz
from pptx import Presentation
from docx import Document

def extract_text(file_path):
    if file_path.endswith('.pdf'):
        return extract_pdf(file_path)
    elif file_path.endswith('.pptx'):
        return extract_ppt(file_path)
    elif file_path.endswith('.docx'):
        return extract_docx(file_path)
    return ""

def extract_pdf(path):
    text = ""
    doc = fitz.open(path)
    for page in doc:
        text += page.get_text()
    return text

def extract_ppt(path):
    text = ""
    prs = Presentation(path)
    for slide in prs.slides:
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                text += shape.text + " "
    return text

def extract_docx(path):
    doc = Document(path)
    return " ".join([p.text for p in doc.paragraphs])
