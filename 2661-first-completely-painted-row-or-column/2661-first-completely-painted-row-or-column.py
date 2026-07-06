class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        hashmap={}
        rows=len(mat)
        cols=len(mat[0])
        for i in range(rows):
            for j in range(cols):
                hashmap[mat[i][j]]=(i,j)
        rowc=[cols]*rows
        colc=[rows]*cols
        for ind,ele in enumerate(arr):
            i,j=hashmap[ele]
            rowc[i]-=1
            if rowc[i]==0:
                return ind
            colc[j]-=1
            if colc[j]==0:
                return ind
        
