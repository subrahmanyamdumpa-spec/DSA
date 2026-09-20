class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        position = 1

        for ch in s:
            alphabet_pos = ord(ch) - ord('a') + 1
            reverse_pos = 27 - alphabet_pos
            ans += position * reverse_pos
            position += 1

        return ans