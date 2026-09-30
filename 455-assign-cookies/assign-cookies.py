class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        count = 0
        j = 0
        for i in range(len(s)):
            if j < len(g) and s[i] >= g[j]:
                count += 1
                j += 1
        return count