class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        handmadeCounter = defaultdict(int)

        for i in nums:
            handmadeCounter[i] += 1
        
        for i in handmadeCounter.values():
            if i > 2:
                return False
        return True