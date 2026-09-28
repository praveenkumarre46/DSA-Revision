class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        know = {k: v for k, v in knowledge}
        res = []
        in_bracket = False
        key_chars = []

        for char in s:
            if char == '(':
                in_bracket = True
            elif char == ')':
                in_bracket = False
                key = "".join(key_chars)
                res.append(know.get(key, "?"))
                key_chars = []
            elif in_bracket:
                key_chars.append(char)
            else:
                res.append(char)

        return "".join(res)