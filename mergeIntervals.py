class Solution(object):
    def merge(self, intervals):
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            lastEndValue = output[-1][1]
            if start <= lastEndValue:
                output[-1][1] = max(lastEndValue, end)
            else:
                output.append([start, end])
        return output