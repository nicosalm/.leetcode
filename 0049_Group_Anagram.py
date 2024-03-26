from typing import List

# Problem: Group Anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        t = {}
        for s in strs:
            s_sorted = ''.join(sorted(s))
            
            if s_sorted not in t:
                t[s_sorted] = []

            t[s_sorted].append(s)

        return list(t.values())

# Time Complexity: O(NKlogK), where N is the length of strs,
# and K is the maximum length of a string in strs. The outer
# loop has complexity O(N) as we iterate through each string.
# Then, we sort each string in O(KlogK) time.
