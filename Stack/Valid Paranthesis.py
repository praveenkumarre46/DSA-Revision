class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {")": "(", "}": "{", "]": "["}
        
        for ele in s:
            if ele in dic:
                if not stack or stack[-1] != dic[ele]:
                    return False
                stack.pop()
            else:
                stack.append(ele)
                
        return not stack