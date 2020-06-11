" Merge Intervals "

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals)):
            if len(res)==0 :
                res.append(intervals[i])
            elif intervals[i][0]>res[-1][1]:
                res.append(intervals[i])
            else:
                start,end=res.pop()
                end=max(end,intervals[i][1])
                res.append([start,end])
        return res
