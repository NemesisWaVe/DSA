class Solution:
    def maxArea(self, height: List[int]) -> int:
        f=0
        r=len(height)-1
        maxArea=0
        while f<r:
            h=min(height[f],height[r])
            area=h*(r-f)
            maxArea=max(area,maxArea)
            if height[f]<height[r]:
                f+=1
            else:
                r-=1
        return maxArea