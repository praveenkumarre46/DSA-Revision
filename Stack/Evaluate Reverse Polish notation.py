class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ele in tokens:
            if ele == "+":
                stack.append(stack.pop() + stack.pop())
            elif ele == "-":
                op2, op1 = stack.pop(), stack.pop()
                stack.append(op1 - op2)
            elif ele == "*":
                stack.append(stack.pop() * stack.pop())
            elif ele == "/":
                op2, op1 = stack.pop(), stack.pop()
                stack.append(int(op1 / op2))
            else:
                stack.append(int(ele))
        return stack[0]