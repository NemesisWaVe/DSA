class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0 # Keeps track of the biggest area found so far

        while l < r:
            # 1. Calculate Area for current window
            Width = (r - l)
            Height = min(height[l], height[r])
            area = (r - l) * min(height[l], height[r])
            
            # 2. Update max result
            res = max(res, area)

            # 3. GREEDY MOVE: Move the shorter pointer inward
            if height[l] < height[r]:
                l += 1
            else:
                r-=1
                
        return res