class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda interval: interval[0])
        print(intervals)
        output = [intervals[0]]
        for eachinterval in intervals[1:]:
            if len(output) == 0 or output[-1][1] < eachinterval[0]:
                output.append(eachinterval)
            else:
                output[-1] = [min(output[-1][0], eachinterval[0]), max(output[-1][1], eachinterval[1])]
        return output