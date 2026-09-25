class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = [[]]
        
        for char in expression:
            if char.isalpha():
                if stack[-1] and isinstance(stack[-1][-1], set):
                    stack[-1].append({char})
                else:
                    stack[-1].append({char})
            elif char == '{':
                stack.append([])
            elif char == ',':
                pass 
            elif char == '}':
                pass

        stack = [[]]  
        groups = [[]] 
        level_stack = []

        for char in expression:
            if char.isalpha():
                if not groups[-1]:
                    groups[-1].append({char})
                else:
                    groups[-1][-1] = {a + b for a in groups[-1][-1] for b in {char}}
            elif char == '{':
                level_stack.append(groups)
                groups = [[]]
            elif char == ',':
                groups.append([])
            elif char == '}':
                combined_set = set()
                for group in groups:
                    curr = {""}
                    for s in group:
                        curr = {a + b for a in curr for b in s}
                    combined_set.update(curr)
                
                groups = level_stack.pop()
                if not groups[-1]:
                    groups[-1].append(combined_set)
                else:
                    groups[-1][-1] = {a + b for a in groups[-1][-1] for b in combined_set}

        final_set = set()
        for group in groups:
            curr = {""}
            for s in group:
                curr = {a + b for a in curr for b in s}
            final_set.update(curr)

        return sorted(list(final_set))