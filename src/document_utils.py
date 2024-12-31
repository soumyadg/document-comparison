import difflib
from docx import Document

def read_docx(file_path):
    """
    Reads a DOCX file and extracts all non-empty paragraphs.
    """
    doc = Document(file_path)
    return [paragraph.text for paragraph in doc.paragraphs if paragraph.text]

def compare_documents(doc1, doc2):
    """
    Compares two document contents line by line to identify changes.
    """
    doc1_text = '\n'.join(doc1)
    doc2_text = '\n'.join(doc2)
    
    diff = list(difflib.unified_diff(doc1_text.splitlines(), doc2_text.splitlines(), lineterm=''))
    return [line for line in diff if line.startswith('+') or line.startswith('-')]

def summarize_changes(changes):
    """
    Generates a summary of document changes using a simple method.
    """
    return " ".join(changes)

def format_summary_as_points(summary):
    """
    Formats the summary text into bullet points for easier reading.
    """
    sentences = summary.split('. ')
    bullet_points = "\n".join(f"- {sentence.strip()}" for sentence in sentences if sentence)
    return bullet_points
