class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        path=[]
        res=[]
        def backtrack(i,path):
            if i==len(nums):
                res.append(path.copy())
                return
            path.append(nums[i])   #takes nums[i]
            backtrack(i+1,path)    
            path.pop()
        #Dont take nums[i] or pop 
            backtrack(i+1,path)
        backtrack(0,[])
        return res           
        