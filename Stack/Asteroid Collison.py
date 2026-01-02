class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        
        for ele in asteroids:
            while stack and ele < 0 < stack[-1]:
                if stack[-1] < -ele:
                    stack.pop()
                    continue
                elif stack[-1] == -ele:
                    stack.pop()
                break
            else:
                stack.append(ele)
                
        return stack