class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen_numbers=set()
        for num in nums:
            if num in seen_numbers:
                return True
            seen_numbers.add(num)
        return False          
        