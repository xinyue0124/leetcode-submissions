class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        i1, i2 = -1, -1
        shortest = len(wordsDict)
        for i, w in enumerate(wordsDict):
            if w == word1:
                i1 = i
            elif w == word2:
                i2 = i
            if i1 != -1 and i2 != -1:
                shortest = min(shortest, abs(i1 - i2))
        return shortest

        