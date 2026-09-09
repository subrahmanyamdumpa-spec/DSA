class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max=0
        cur_min=0
        max_sum=nums[0]
        min_sum=nums[0]
        total_sum=0
        for i in range(len(nums)):
            cur_max=max(cur_max+nums[i],nums[i])
            max_sum=max(max_sum,cur_max)
            cur_min=min(cur_min+nums[i],nums[i])
            min_sum=min(min_sum,cur_min)
            total_sum+=nums[i]
        if max_sum<0:
             return max_sum
        return max(max_sum,total_sum-min_sum)
        