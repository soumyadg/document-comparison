from document_utils import read_docx, compare_documents, summarize_changes, format_summary_as_points

def main():
    """
    Main execution function that orchestrates reading documents, comparing them, summarizing changes,
    and formatting the summary for display.
    """
    # Define paths to your document files
    doc1_path = 'data/Jan_2015.docx'
    doc2_path = 'data/Mar_2023.docx'

    # Read documents from specified paths
    doc1 = read_docx(doc1_path)
    doc2 = read_docx(doc2_path)

    # Compare documents and capture the changes
    changes = compare_documents(doc1, doc2)

    # Summarize the changes using the advanced summarization functionality
    final_summary = summarize_changes(changes)

    # Format the summary into bullet points for easy reading
    formatted_output = format_summary_as_points(final_summary)

    # Output the structured summary to the console
    print("Structured Summary of Changes:")
    print(formatted_output)

if __name__ == "__main__":
    main()
