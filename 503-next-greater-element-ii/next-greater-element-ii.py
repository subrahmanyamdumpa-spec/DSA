class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(2 * n):
            while stack and nums[i % n] > nums[stack[-1]]:
                idx = stack.pop()
                res[idx] = nums[i % n]
            if i < n:
                stack.append(i)
        return res