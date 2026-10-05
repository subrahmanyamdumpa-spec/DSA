class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        a=[]
        for i in range(m):
            a.append(nums1[i])
        for j in range(n):
            a.append(nums2[j])
        a.sort()
        for i in range(m + n):
            nums1[i] = a[i]

        