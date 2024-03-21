from collections import defaultdict

# Problem: Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count = defaultdict(int)
        
        # count the frequency of characters in string s
        for char in s:
            count[char] += 1
        
        # decrement the frequency of characters in string t
        for char in t:
            count[char] -= 1
        
        # check if any character has non-zero frequency
        for val in count.values():
            if val != 0:
                return False
        
        return True

# Time complexity: O(n) where n is the length of the input strings s and t
