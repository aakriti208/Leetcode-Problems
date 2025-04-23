class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        index = 0
        start, end = newInterval[0], newInterval[1]
        while index < len(intervals) and start > intervals[index][1]:
            res.append(intervals[index])
            index += 1
        while index < len(intervals) and end >= intervals[index][0]:
            start = min(start, intervals[index][0])
            end = max(end, intervals[index][1])
            index += 1
        res.append([start, end])
        while index < len(intervals):
            res.append(intervals[index])
            index += 1
        return res

