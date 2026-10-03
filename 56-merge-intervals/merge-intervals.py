class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        result=[intervals[0]]
        for i in range(1,len(intervals)):
            cur=intervals[i]
            if cur[0]<=result[-1][1]:
                result[-1][1]=max(result[-1][1],cur[1])
            else:
                result.append(cur)
        return result
        