from bisect import bisect_left,bisect_right
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left=bisect_left(nums,target)
        right=bisect_right(nums,target)
        if left==right:
            return [-1,-1]
        return [left,right-1]

        