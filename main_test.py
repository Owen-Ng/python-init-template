import unittest
from main import main
from unittest.mock import patch
from utils.str_utils import RemoveTrailingNewLine

def readfileToStr(path):
    res = []
    with open(path, 'r') as rf:
        for line in rf.readlines():
            res.append(RemoveTrailingNewLine(line))
    return "\n".join(res)
class TestMain(unittest.TestCase):

    @patch('builtins.input', return_value='./test_files/test1_input.txt')
    def test1_main(self, input):
        self.assertEqual(main(), readfileToStr("./test_files/test1_output.txt"))
    
    @patch('builtins.input', return_value='./test_files/test2_input.txt')
    def test2_main(self, input):
        self.assertEqual(main(), readfileToStr("./test_files/test2_output.txt"))

if __name__ == '__main__':
    unittest.main()