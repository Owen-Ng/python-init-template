import unittest
from main import main
from unittest.mock import patch

class TestMain(unittest.TestCase):

    @patch('builtins.input', return_value='./tests/test1')
    def test_main(self, input):
        self.assertEqual(main(), 524288)

    # @patch('main.main', return_value='yes')
    # def test_mock_main(self, main):
    #     self.assertEqual(main(), 'yes')

if __name__ == '__main__':
    unittest.main()