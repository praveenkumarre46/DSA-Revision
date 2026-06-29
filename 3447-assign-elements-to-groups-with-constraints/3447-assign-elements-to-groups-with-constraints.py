class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        smallind = {}
        for i, ele in enumerate(elements):
            if ele not in smallind:
                smallind[ele] = i
                
        assigned = []
        
        for group in groups:
            best_index = float('inf')
            
            for i in range(1, int(group**0.5) + 1):
                if group % i == 0:
                    if i in smallind:
                        best_index = min(best_index, smallind[i])
                    
                    other_divisor = group // i
                    if other_divisor in smallind:
                        best_index = min(best_index, smallind[other_divisor])
            
            if best_index != float('inf'):
                assigned.append(best_index)
            else:
                assigned.append(-1)
                
        return assigned