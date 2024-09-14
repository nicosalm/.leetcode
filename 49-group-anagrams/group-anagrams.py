class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        t = defaultdict(list)
        for s in strs:
            s_sorted = ''.join(sorted(s))
            t[s_sorted].append(s)
        return t.values()