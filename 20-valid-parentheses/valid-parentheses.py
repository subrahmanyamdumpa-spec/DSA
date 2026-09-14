class Solution:
    def isValid(self, s):

        stack = []
        hashmap = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for ch in s:

            if ch not in hashmap:
                stack.append(ch)

            else:
                if not stack or stack[-1] != hashmap[ch]:
                    return False

                stack.pop()

        return len(stack) == 0
    
        
        