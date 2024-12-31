import difflib
from docx import Document
import openai
import warnings
import re
from summarizer import Summarizer

# Set up warnings to ignore non-critical messages
warnings.filterwarnings("ignore", message="Some weights of the model checkpoint at bert-large-uncased were not used when initializing BertModel")
warnings.filterwarnings("ignore", category=FutureWarning, message="The default value of `n_init` will change from 10 to 'auto' in 1.4.")

# Configure the OpenAI GPT API key
openai.api_key = "OpenAI Key"

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
    Processes and summarizes document changes using GPT-3.5.
    """
    changes_text = ' '.join(changes)
    chunks = [changes_text[i:i + 200] for i in range(0, len(changes_text), 200)]
    summaries = []
    for chunk in chunks:
        summary = process_chunk(chunk)
        if summary:
            summaries.append(summary)
    combined_summary = ' '.join(summaries)
    if len(combined_summary.split()) > 16000:
        combined_summary = second_pass_summary(combined_summary)
    return combined_summary

def process_chunk(chunk):
    """
    Calls the OpenAI API to summarize a chunk of text.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Provide a concise summary."},
                {"role": "user", "content": f"Summarize this text: {chunk}"}
            ],
            max_tokens=300
        )
        return response.choices[0].message['content']
    except Exception as e:
        print(f"Error processing chunk: {e}")
        return None

def second_pass_summary(text):
    """
    Handles a second pass of summarization if the initial summary is too long.
    """
    chunks = [text[i:i + 16000] for i in range(0, len(text), 16000)]
    final_summaries = []
    for chunk in chunks:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Provide a final comprehensive summary."},
                    {"role": "user", "content": f"Provide a final summary of these changes: {chunk}"}
                ],
                max_tokens=1024
            )
            final_summaries.append(response.choices[0].message['content'])
        except Exception as e:
            print(f"Error in final summarization: {e}")
            final_summaries.append("Final summary process failed.")
    return ' '.join(final_summaries)

def format_summary_as_points(summary_text):
    """
    Formats a summary into bullet points for easier reading.
    """
    sentences = re.split(r'\. |\.\n', summary_text)
    unique_sentences = set(filter(None, sentences))
    bullet_points = "\n".join(f"- {sentence.strip()}" for sentence in unique_sentences if len(sentence.strip()) > 3)
    return bullet_points
