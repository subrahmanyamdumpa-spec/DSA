class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n=len(numbers)
        l=0
        r=n-1
        while l<r:
            res=numbers[l]+numbers[r]
            if res==target:
                return l+1,r+1
            elif res>target:
                r-=1
            else:
                l+=1
        return res



        