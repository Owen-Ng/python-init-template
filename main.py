from sortedcontainers import SortedList
import requests
from utils.str_utils import RemoveTrailingNewLine
import heapq
def main():
    arg = input("Input file Path\n")
    wordToCount = {}
    with open(arg, "r") as rf:
        for line in rf.readlines():
            line = RemoveTrailingNewLine(line)
            for word in line.split(" "):
                if word not in wordToCount:
                    wordToCount[word] = 0
                wordToCount[word] += 1

    sortedWordToCount = []

    for k,v in wordToCount.items():
        heapq.heappush(sortedWordToCount, [k,str(v)])
    
    res = []

    while (len(sortedWordToCount) > 0):
        current = heapq.heappop(sortedWordToCount)
        print(" ".join(current))
        res.append( " ".join(current))
    print(res)
    return "\n".join(res)

if __name__ == '__main__':
    response = main()
    print(response)