class Solution:
    def calPoints(self, ops: List[str]) -> int:
        points = []
        for op in ops:
            # print(points, op)
            if op == "C":
                points.pop()
            elif op == "D":
                top = points[-1]
                points.append(2*top)
            elif op == "+":
                points.append(points[-1] + points[-2])
            else:
                points.append(int(op))
        return sum(points)