import heapq
class WordsController:
    
    def __init__(self, words):
        self.words = words

    def WordCountLexicalOrder(self):
        wordToCount = {}
        for word in self.words:
            if word not in wordToCount:
                wordToCount[word] = 0
            wordToCount[word] += 1

        sortedWordToCount = []

        for k,v in wordToCount.items():
            heapq.heappush(sortedWordToCount, [k,str(v)])
        
        res = []

        while (len(sortedWordToCount) > 0):
            current = heapq.heappop(sortedWordToCount)
            res.append( " ".join(current))
        return res