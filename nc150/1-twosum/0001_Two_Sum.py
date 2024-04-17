from typing import List

# Problem: Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sums = {} # difference dictionary

        for idx, num in enumerate(nums):
            complement = target - num
            if complement in sums:
                return [sums[complement], idx]
            else:
                sums[num] = idx

        return [-1]
        
# Time, Space: O(n), O(n)
