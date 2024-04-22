class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = 0 
        charset = set()
        l = 0

        for r in range(len(s)):
            # if char not in charset, add it and compare to max_len
            if s[r] not in charset:
                charset.add(s[r])
                max_len = max(r-l+1, max_len)
            # advance l until all chars in set are unique again
            else:
                while s[r] in charset:
                    charset.remove(s[l])
                    l += 1
                charset.add(s[r])

        return max_len
                