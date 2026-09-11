class Solution:
    def isPalindrome(self, s: str) -> bool: 
        clean=""
        for ch in s.lower():
            if ch.isalnum():
                clean+=ch
        return clean==clean[::-1]
        
        
        
        