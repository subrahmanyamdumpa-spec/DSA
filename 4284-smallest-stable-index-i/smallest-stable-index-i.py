class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Build suffix minimum array
        rightMin = [0] * n
        rightMin[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            rightMin[i] = min(nums[i], rightMin[i + 1])

        # Traverse with prefix maximum
        leftMax = 0

        for i in range(n):
            leftMax = max(leftMax, nums[i])

            if leftMax - rightMin[i] <= k:
                return i

        return -1