# Trapping Rain Water (Hard)

# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.

# Notes: This is easily solved with a dp / divide and conquer approach.

class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0

        l_max, r_max = 0, 0
        l, r = 0, len(height) - 1
        water = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] > l_max:
                    l_max = height[l]
                else:
                    water += l_max - height[l]
                l += 1
            else:
                if height[r] > r_max:
                    r_max = height[r]
                else:
                    water += r_max - height[r]
                r -= 1

        return water
