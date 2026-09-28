class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        count=0
        for c in s:
            if c==")":
                if stack and stack[-1]=="(":
                    stack.pop()
            elif c=="(":
                stack.append(c)
            count=max(count,len(stack))
        return count