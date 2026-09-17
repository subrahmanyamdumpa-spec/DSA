class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n=len(nums)
        left=0
        right=n-1
        res=[0]*n
        k=n-1
        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                res[k]=nums[left]*nums[left]
                left+=1
            else:
                res[k]=nums[right]*nums[right]
                right-=1
            k-=1
        return res
        