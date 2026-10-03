class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        l=0
        n=len(cardPoints)
        r=n-1
        l_sum=0
        r_sum=0
        maxi=float("inf")
        for i in range(k):
            l_sum+=cardPoints[i]
            maxi=l_sum
        for i in range(k-1,-1,-1):
            l_sum-=cardPoints[i]
            r_sum+=cardPoints[r]
            maxi=max(l_sum+r_sum,maxi)
            r-=1
        return maxi
        
        

     
                




        