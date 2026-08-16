class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        maxProf=0
        while r<len(prices):
            currProf=0
            if prices[l]<prices[r]:
                currProf=prices[r]-prices[l]
                maxProf=max(maxProf,currProf)
            else:
                l=r
            r+=1
        return maxProf