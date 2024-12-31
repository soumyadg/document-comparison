import unittest
from unittest.mock import patch
from src.document_utils import read_docx, compare_documents, summarize_changes, format_summary_as_points

class TestDocumentUtils(unittest.TestCase):

    @patch('src.document_utils.Document')
    def test_read_docx(self, mock_doc):
        # Setup
        mock_doc.return_value.paragraphs = [
            type('Paragraph', (object,), {'text': 'Hello World'}),
            type('Paragraph', (object,), {'text': ''}),
            type('Paragraph', (object,), {'text': 'Another line'})
        ]

        # Execute
        result = read_docx('dummy_path')

        # Assert
        self.assertEqual(result, ['Hello World', 'Another line'])

    def test_compare_documents(self):
        # Define documents
        doc1 = ["Hello world."]
        doc2 = ["Hello world.", "New line here."]

        # Expected result
        expected = ['+ New line here.']

        # Test
        result = compare_documents(doc1, doc2)
        self.assertEqual(result, expected)

    def test_summarize_changes(self):
        # Setup
        changes = ['+ New line here.', '- Old line gone.']

        # Expected summary
        expected = 'New line here. Old line gone.'

        # Using a mock to simulate API behavior
        with patch('src.document_utils.process_chunk', return_value='New line here. Old line gone.'):
            result = summarize_changes(changes)

        # Verify
        self.assertEqual(result, expected)

    def test_format_summary_as_points(self):
        # Setup
        summary_text = "Line one. Line two."

        # Expected formatted output
        expected = "- Line one\n- Line two"

        # Test
        result = format_summary_as_points(summary_text)

        # Verify
        self.assertEqual(result, expected)

# This allows the test suite to be run from the command line
if __name__ == '__main__':
    unittest.main()
