class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result=[]
        win_s={}
        win_p={}
        for ch in p:
            win_p[ch]=win_p.get(ch,0)+1
        left=0
        for right in range(len(s)):
            win_s[s[right]]=win_s.get(s[right],0)+1
            if right-left+1 > len(p):
                win_s[s[left]]-=1
                if win_s[s[left]]==0:
                    del win_s[s[left]]
                left+=1
            if win_p==win_s:
                result.append(left)
        return result
             
            
        