import unittest
from main import main
from unittest.mock import patch

class TestMain(unittest.TestCase):

    @patch('builtins.input', return_value='yes')
    @patch('main.arg1', return_value='yes')
    @patch('main.arg2', return_value='yes')
    def test_main(self, input, arg1,arg2):
        self.assertEqual(main(), 'yesyesyes')

    @patch('main.main', return_value='yes')
    def test_mock_main(self, main):
        self.assertEqual(main(), 'yes')

if __name__ == '__main__':
    unittest.main()