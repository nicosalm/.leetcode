class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums) # set of all numbers in list
        longest = 0

        for n in nums: # for each number
            if (n-1) not in numset: # only assess numbers which do not have predecessors
                streak = 0
                while (n + streak) in numset: # count upwards
                    streak += 1
                longest = max(longest, streak) # replace count if length > counter
        
        return longest