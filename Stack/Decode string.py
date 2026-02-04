class Solution:
    def decodeString(self, s: str) -> str:
        countStack = []
        stringStack = []
        curr = ""
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == "[":
                countStack.append(num)
                stringStack.append(curr)
                num = 0
                curr = ""

            elif ch == "]":
                k = countStack.pop()
                prev = stringStack.pop()
                curr = prev + curr * k   
            else:
                curr += ch

        return curr
