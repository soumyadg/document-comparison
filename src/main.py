from document_utils import read_docx, compare_documents, summarize_changes, format_summary_as_points

def main():
    # Define the paths to your documents
    doc1_path = 'data/Jan_2015.docx'
    doc2_path = 'data/Mar_2023.docx'

    # Read and compare documents
    doc1 = read_docx(doc1_path)
    doc2 = read_docx(doc2_path)
    changes = compare_documents(doc1, doc2)

    # Summarize changes and format the summary into bullet points
    final_summary = summarize_changes(changes)
    formatted_output = format_summary_as_points(final_summary)

    # Print the structured summary
    print("Structured Summary of Changes:")
    print(formatted_output)

if __name__ == "__main__":
    main()
