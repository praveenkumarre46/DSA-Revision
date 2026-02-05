class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        def bs(submat,tar):
            low=0
            high=len(submat)-1
            while low<=high:
                mid=low+(high-low)//2
                if submat[mid]==tar:
                    return True
                elif submat[mid]<tar:
                    low=mid+1
                else:
                    high=mid-1
            return False
        r,c=0,0
        while r<row:
            if matrix[r][0] <= target <= matrix[r][-1]:
                return bs(matrix[r],target)
            else:
                r+=1
        return False
        