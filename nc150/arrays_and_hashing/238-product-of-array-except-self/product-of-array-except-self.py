class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # in = [1, 2, 3, 4]
        # out = [24, 12, 8, 6]
        # res = [1, 1, 1, 1] => (after first loop) [1, 1, 2, 6] => (second pass) [24, 12, 8, 6]

        res = [1] * len(nums) # result array with initial inputs of 1

        prefix = 1 # before i
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        postfix = 1 # after i
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res # end result is the accumulated product of all indices before i and after i

# Notes: You only store results in `res`, you never read from it when doing multiplication.
# O(n) time, O(1) space