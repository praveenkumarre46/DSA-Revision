class Solution:
    def calPoints(self, operations: List[str]) -> int:
        fin = []
        for ele in operations:
            if ele == "+":
                fin.append(fin[-1] + fin[-2])
            elif ele == "D":
                fin.append(fin[-1] * 2)
            elif ele == "C":
                fin.pop()
            else:
                fin.append(int(ele))
        return sum(fin)