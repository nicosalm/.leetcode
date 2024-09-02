class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        handmadeCounter = collections.Counter(nums)
        
        for i in handmadeCounter.values():
            if i > 2:
                return False
        return True