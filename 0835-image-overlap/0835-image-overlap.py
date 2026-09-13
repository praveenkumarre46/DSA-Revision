class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        pts1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        pts2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        shift_counts = collections.Counter()
        max_overlap = 0
        
        for r1, c1 in pts1:
            for r2, c2 in pts2:
                shift = (r2 - r1, c2 - c1)
                shift_counts[shift] += 1
                max_overlap = max(max_overlap, shift_counts[shift])
                
        return max_overlap