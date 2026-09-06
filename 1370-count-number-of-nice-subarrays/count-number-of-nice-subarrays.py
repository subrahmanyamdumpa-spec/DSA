class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def Atmost(k):
            left=0
            odd=0
            count=0
            for right in range(len(nums)):
                if nums[right]%2==1:
                    odd+=1
                while odd>k:
                    if nums[left]%2==1:
                        odd-=1
                    left+=1
                count+=right-left+1
            return count
        return Atmost(k)-Atmost(k-1)       