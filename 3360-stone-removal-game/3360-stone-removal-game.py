class Solution:
    def canAliceWin(self, n: int) -> bool:
        i = 10
        a = 1
        while n >= i:
            n -= i
            i -= 1
            a += 1
        return a % 2 == 0