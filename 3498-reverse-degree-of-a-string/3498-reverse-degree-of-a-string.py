class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((26 - (ord(char) - ord('a'))) * i for i, char in enumerate(s, 1))