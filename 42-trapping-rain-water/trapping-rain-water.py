class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        lBest=height[0]
        rBest=height[len(height)-1]
        l=0
        r=len(height)-1
        water=0
        while l<r:
            if lBest<=rBest:
                l+=1
                lBest=max(height[l],lBest)
                water+=lBest-height[l]
            elif rBest<lBest:
                r-=1
                rBest=max(height[r],rBest)
                water+=rBest-height[r]
        return water
                
