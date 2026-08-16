class Solution:
    def maxArea(self, height: List[int]) -> int:
        f=0
        r=len(height)-1
        maxWater=0
        while f<r:
            width=r-f
            currHeight=min(height[f],height[r])
            currArea=width*currHeight
            maxWater=max(currArea,maxWater)
            if height[f]<height[r]:
                f+=1
            else:
                r-=1
        return maxWater