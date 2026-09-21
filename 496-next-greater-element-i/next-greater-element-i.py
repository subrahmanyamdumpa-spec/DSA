class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack=[]
        hashmap={}
        for num in nums2:
            while stack and num>stack[-1]:
                popped=stack.pop()
                hashmap[popped]=num
            stack.append(num)
        while stack:
            popped=stack.pop()
            hashmap[popped]=-1
        res=[]
        for num in nums1:
            res.append(hashmap[num])
        return res
