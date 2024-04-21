class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l, r = 0, len(height) - 1
        area_max = 0 

        while l < r: 
            area_curr = min(height[l], height[r]) * (r - l) # find the lower wall, then multiply by width
            area_max = max(area_curr, area_max)

            if height[l] < height[r]:
                l += 1

            else:
                r -= 1

        return area_max