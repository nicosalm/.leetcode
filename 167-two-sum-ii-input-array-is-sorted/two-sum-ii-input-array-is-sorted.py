class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        # want sum(l, r) = target
        while l < r:
            if nums[l] + nums[r] == target: return (l + 1, r + 1)
            if nums[l] + nums[r] > target: r -= 1
            else: l += 1