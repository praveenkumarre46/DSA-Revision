class Solution:

  def reverseParentheses(self, s: str) -> str:
    stack = []

    for c in s:
      if c == ")":
        subs = []
        while stack and stack[-1] != "(":
          subs.append(stack.pop())

        stack.pop()
        stack.extend(subs)
      else:
        stack.append(c)

    return "".join(stack)