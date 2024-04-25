from sortedcontainers import SortedList
import requests
from utils.str_utils import RemoveTrailingNewLine
def main():
    arg = input("Input file Path\n")
    res = []
    with open(arg, "r") as rf:
        for line in rf.readlines():
            res.append(RemoveTrailingNewLine(line))
    return "\n".join(res)
if __name__ == '__main__':
    response = main()
    print(response)