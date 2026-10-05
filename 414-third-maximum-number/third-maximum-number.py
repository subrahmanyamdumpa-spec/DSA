class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        l=list(set(nums))
        if len(l)<3:
            return max(l)
        else:
            l.sort()
            l.reverse()
            return l[2]
        