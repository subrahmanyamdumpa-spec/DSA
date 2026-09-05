class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum=sum(nums[:k])
        maxi=window_sum
        for right in range(k,len(nums)):
            window_sum+=nums[right]
            window_sum-=nums[right-k]
            maxi=max(maxi,window_sum)
        return maxi/k
                         

        