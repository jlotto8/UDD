import unittest
import io
from unittest.mock import patch
from try_except import words_uu

class TestWordsUUFunction(unittest.TestCase):
    def test_words_uu_file_found(self):
        # Test when the file is found and contains words
        with patch('builtins.open', return_value=io.StringIO("Word1\nWord2\nWord3\nVACUUM4")):
            result = words_uu('dummy_path.txt')
            self.assertEqual(result, ['VACUUM4'])

    def test_words_uu_file_not_found(self):
        # Test when the file is not found
        with self.assertRaises(FileNotFoundError):
            words_uu('nonexistent_file.txt')

    def test_words_uu_empty_file(self):
        # Test when the file is found but empty
        with patch('builtins.open', return_value=io.StringIO("")):
            with self.assertRaises(ValueError) as context:
                words_uu('empty_file.txt')
            self.assertEqual(str(context.exception), "Error: File is empty.")

    def test_words_uu_io_error(self):
        # Test when an IO error occurs while reading the file
        with patch('builtins.open', side_effect=IOError("Mocked IO Error")):
            with self.assertRaises(IOError) as context:
                words_uu('error_file.txt')
            self.assertEqual(str(context.exception), "Mocked IO Error")


if __name__ == '__main__':
    unittest.main()                                         