class Solution:
    def canJump(self, nums):
        maxi = 0

        for i in range(len(nums)):

            if i > maxi:
                return False

            maxi = max(maxi, i + nums[i])

            if maxi >= len(nums) - 1:
                return True

        return False