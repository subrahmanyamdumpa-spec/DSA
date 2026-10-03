class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        last_end=intervals[0][1]
        count=0
        for i in range(1,len(intervals)):
            if intervals[i][0]<last_end:
                count+=1
            else:
                last_end=intervals[i][1]
        return count
        