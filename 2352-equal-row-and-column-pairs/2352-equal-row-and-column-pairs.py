class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        col_freq = {}
        
        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            
            col_tuple = tuple(col)
            if col_tuple in col_freq:
                col_freq[col_tuple] += 1
            else:
                col_freq[col_tuple] = 1
                
        res = 0
        for row in grid:
            row_tuple = tuple(row)
            if row_tuple in col_freq:
                res += col_freq[row_tuple]
                
        return res