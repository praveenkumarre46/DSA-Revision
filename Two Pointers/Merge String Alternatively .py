class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for char1, char2 in zip(word1, word2):
            res.append(char1)
            res.append(char2)
        
        res.append(word1[len(word2):])
        res.append(word2[len(word1):])
        
        return "".join(res)