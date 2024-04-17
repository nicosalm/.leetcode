from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        '''
        Below, defaultdict(int) creates a dictionary where accessing a new key automatically initializes its value to 0, 
        the default int() return value. As characters from the string s are processed, the dictionary adjusts the counts,
        automatically setting unseen characters to 0 before incrementing or decrementing their values.
        '''
        
        count = defaultdict(int)
        
        # count the frequency of characters in string s
        for char in s:
            count[char] += 1
        
        # decrement the frequency of characters in string t
        for char in t:
            count[char] -= 1
        
        # if any character has non-zero frequency => not anagram
        for val in count.values():
            if val != 0:
                return False
        
        return True 
        
        
# Time, Space: O(n), O(n)
