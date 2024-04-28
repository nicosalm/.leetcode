class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        res = set()
        
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            target = 0 - nums[i] # 0 = target + nums[i]
            
            while l < r:
                if nums[l] + nums[r] == target:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1

                elif nums[l] + nums[r] < target: 
                    l += 1
                else: 
                    r -= 1

        return res