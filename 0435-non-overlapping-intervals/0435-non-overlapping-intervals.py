class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        result = [intervals[0]]

        for start,end in intervals[1:]:

            if start < result[-1][1]:
                result[-1][1] = min(end, result[-1][1])
            else:
                result.append([start,end])

        return  len(intervals) - len(result)
