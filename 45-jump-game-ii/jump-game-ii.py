class Solution:
    def jump(self, nums):
        count = 0
        maxi = 0
        current_end = 0

        for i in range(len(nums) - 1):
            maxi = max(maxi, i + nums[i])

            if i == current_end:
                count += 1
                current_end = maxi

        return count