
# Document Comparison Tool

## Project Overview

The Document Comparison Tool is designed to assist legal and documentation teams by summarizing and highlighting changes between different versions of documents, specifically focusing on DOCX files. This tool employs a combination of Python libraries and Large Language Models (LLMs), including GPT from OpenAI, to process, compare, and summarize document contents effectively.

## Features

- **Document Reading**: Utilizes `python-docx` to read and extract content from DOCX files.
- **Change Detection**: Implements `difflib` to detect and outline changes between document versions.
- **Summarization**: Leverages OpenAI's GPT models to summarize changes in a concise format.
- **Enhanced Readability**: Formats summaries into structured bullet points for better clarity.

## Getting Started

### Prerequisites

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

Your Name - [soumya_02@outlook.com](mailto:soumya_02@outlook.com)

Project Link: [https://github.com/your-username/document-comparison](https://github.com/your-username/document-comparison)

## Acknowledgments

- [python-docx](https://python-docx.readthedocs.io/en/latest/) for document handling.
- [OpenAI](https://www.openai.com/) for providing the API used for summarizations.
- All contributors who participate in this project.
