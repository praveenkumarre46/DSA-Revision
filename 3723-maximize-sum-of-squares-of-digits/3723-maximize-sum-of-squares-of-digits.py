class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        fins=""
        finsum=0
        n=sum
        for i in range(num):
            if sum>9:
                fins+="9"
                sum-=9
                finsum+=9
            else:
                fins+=str(sum)
                finsum+=sum
                sum-=sum
        return fins if finsum==n else ""
        
        