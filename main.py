from sortedcontainers import SortedList
from utils.str_utils import RemoveTrailingNewLine
from utils.list_utils import ListToWords
from controller.words_controller import WordsController

def main():
    arg = input("Input file Path\n")
    lines = []
    with open(arg, "r") as rf:
        for line in rf.readlines():
            lines.append(line)

    words = ListToWords(lines)

    wordsController = WordsController(words)

    sortedWordCount = wordsController.WordCountLexicalOrder()

    return "\n".join(sortedWordCount)

if __name__ == '__main__':
    response = main()
    print(response)