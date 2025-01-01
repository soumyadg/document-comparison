# Document Comparison Tool
![](llm.png)

# Assignment overview documentation: Document Change Summarizer
#### Jupyter Code in repo: code_jupyter.ipynb

This project involves a script designed to compare two versions of a document and summarize the changes using both GPT-3.5 and BERT models. Below is a step-by-step explanation of the process:

## Overview

The script performs several key functions:
1. Reads two document versions.
2. Compares these documents to identify changes.
3. Summarizes these changes using two different methods: GPT-3.5 and BERT (alternative method to LLMs).
4. Formats and presents the summarized changes in a readable format.

## Detailed Steps

### 1. **Read the Documents**
- **Function**: `Read_docx(file_path)`
- **Purpose**: To extract non-empty paragraphs from a DOCX file. This helps in processing documents that are structured in paragraphs, skipping empty paragraphs that do not contain useful information.
- **Input**: File path to the DOCX document.
- **Output**: List of non-empty paragraphs from the document.

### 2. **Compare Documents**
- **Function**: `Compare_documents(doc1, doc2)`
- **Purpose**: To identify textual changes between two versions of a document. It uses the `difflib.unified_diff` to generate differences in an easily understandable manner.
- **Input**: Lists of strings (document contents split into lines).
- **Output**: List of changes detected, marked with '+' for additions or '-' for deletions.

### 3. **Summarize Changes Using GPT-3.5**
- **Function**: `Summarize_changes(changes, chunk_size=200)`
- **Purpose**: To divide the document changes into manageable chunks and use OpenAI's API to generate summaries for each chunk, which are then combined into a final comprehensive summary.
- **Input**: List of change strings and a chunk size defining how many characters each chunk will contain.
- **Output**: A comprehensive summary of all changes combined into one string.

#### Sub-function for Processing Each Chunk
- **Function**: `Process_chunk(chunk)`
- **Purpose**: To interact with the OpenAI API, sending text to be summarized and receiving the summarized response.
- **Input**: A chunk of text.
- **Output**: Summarized version of the chunk or an error message if the process fails.

### 4. **Further Process the Summary if Needed**
- **Function**: `Second_pass_summary(text)`
- **Purpose**: Handles a second pass of summarization as the combined text from the initial summaries are too long.
- **Input**: Combined text from initial summarizations.
- **Output**: A final summarized version of the text.

### 5. **Format Summary into Bullet Points**
- **Function**: `Format_summary_as_points(summary_text)`
- **Purpose**: Enhances readability by organizing the summary into clearly defined bullet points, making it easier to scan and comprehend.
- **Input**: The full text of the summary.
- **Output**: Formatted summary where each sentence is a bullet point.

### 6. **Summarize Changes Using BERT - alternative method to LLMs**
- **Function**: `Summarize_changes_bert(changes)`
- **Purpose**: Utilizes a BERT model specifically tuned for extractive summarization tasks to summarize the document changes.
- **Input**: List of textual changes.
- **Output**: An extractive summary capturing the essence of the changes.

### 7. **Further Condense BERT Summary**
- **Function**: `Further_condense_summary_bert(text)`
- **Purpose**: Reduces the length of an already summarized text by applying a higher compression ratio.
- **Input**: Text to condense further, typically already summarized.
- **Output**: A more concise version of the input summary, reduced by the specified ratio.

## Execution Flow

The script begins by reading the two document versions and comparing them to detect changes. If changes are found, it summarizes these changes using both GPT-3.5 and BERT models. The summarized changes are then presented in a structured format to enhance understanding and readability.

## Evaluation of Summary Quality: Understanding ROUGE

### What is ROUGE?
ROUGE, which stands for Recall-Oriented Understudy for Gisting Evaluation, is a set of metrics used for evaluating automatic summarization of texts as well as machine translation. It works by comparing a computer-generated summary or translation against one or more reference summaries (typically produced by humans).

ROUGE is primarily designed to measure the quality of a summary by counting the number of overlapping units such as n-grams, word sequences, and word pairs between the computational and reference summaries. Different used variants of ROUGE are ROUGE-N which measures the overlap of N-grams between the generated and reference texts, the ROUGE-L which considers the longest common subsequence between a candidate summary and a set of reference summaries and finall the ROUGE-S which measures skip-bigram co-occurrence statistics, accounting for sentence-level structure similarity naturally.

### Importance of ROUGE in Summary Evaluation
ROUGE has become a standard for evaluating summarization tasks because it provides a quantitative measure to assess how close the machine-generated summary is to a human-generated one. This metric is crucial for developing and tuning summarization algorithms, as it allows developers to benchmark their systems and track improvements over time. Using ROUGE, developers can systematically compare the effectiveness of different summarization approaches and refine their algorithms based on empirical data.

### Limitation in This Assignment: Lack of Reference Summary
For this assignment, the application of ROUGE as an evaluative metric is not feasible due to the absence of a reference summary. The ROUGE methodology fundamentally relies on a comparison between the machine-generated summary and a human-written reference. In the context of summarizing document changes, preparing such a reference summary involves manually analyzing the changes between two document versions and synthesizing those changes into a coherent summary.

#### Why a Reference Summary is not generated:
- **Time Constraints**: Creating accurate and comprehensive reference summaries is time-consuming.
- **Resource Limitations**: The lack of available domain knowledge to create reference summaries is a significant constraint.
- **Focus of the Assignment**: The primary goal of this assignment is to develop and demonstrate the ability to automate the summarization of document changes without relying on manual efforts, hence this work focusses more on the technological implementation rather than manual evaluation processes.

### Estimation conclusion
While ROUGE is an excellent tool for evaluating summary quality in many contexts, its application is limited in scenarios where no suitable reference summaries are available. In such cases, alternative methods of evaluation, such as user feedback or qualitative analysis, might be more appropriate to assess the effectiveness of summarization algorithms.

# Conclusion

This documentation provides a comprehensive understanding of the processes and functions involved in the document change summarizer project. By detailing each step and its purpose, users and reviewers can easily follow the operations performed by the script.

![](llm2.gif)

## GIT Project information

The Document Comparison Tool is designed to assist legal and documentation teams by summarizing and highlighting changes between different versions of documents, specifically focusing on DOCX files. This tool employs a combination of Python libraries and Large Language Models (LLMs), including GPT from OpenAI, to process, compare, and summarize document contents effectively.

### Prerequisites to run the repo

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)

### Installation

Follow these steps to get your development environment set up:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/document-comparison.git
   cd document-comparison
   ```

2. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

To run the document comparison tool, follow these instructions:

1. Place your DOCX files in the `data/` directory.
2. Modify the paths in `src/main.py` to reflect the filenames of the documents you wish to compare.
3. Execute the script:
   ```bash
   python src/main.py
   ```

### Testing

To run unit tests, use the following command:

```bash
python -m unittest discover -s tests
```

This command will discover and run all tests in the `tests` directory.

## Project Structure

Here is an overview of the project's directory and file structure:

- `src/`: Contains the source code.
  - `main.py`: The main script to run the document comparison tool.
  - `document_utils.py`: Utility functions for reading documents, comparing them, and summarizing changes.
- `data/`: Directory for storing sample DOCX files. Ensure this is populated with your specific files for testing and demonstration.
- `tests/`: Contains unit tests for the project.
  - `test_document_utils.py`: Tests for the utility functions in `document_utils.py`.
- `docs/`: Optional directory for project documentation.
- `requirements.txt`: Lists all dependencies required by the project.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Contact

Soumya Dasgupta - [soumya_02@outlook.com](mailto:soumya_02@outlook.com)

Project Link: [https://github.com/your-username/document-comparison](https://github.com/your-username/document-comparison)

## Acknowledgments

- [python-docx](https://python-docx.readthedocs.io/en/latest/) for document handling.
- [OpenAI](https://www.openai.com/) for providing the API used for summarizations.
- All contributors who participate in this project.


