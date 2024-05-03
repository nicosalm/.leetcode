class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        ones = [i for i, digit in enumerate(s) if digit == '1']
        print(ones)
        if len(ones) < k: return ''

        cands = list(zip(ones, ones[k-1:]))
        print(cands)

        minLen = min(r - l for l, r in cands)
        print(minLen)

        cands = list(filter(lambda x: x[1]-x[0] == minLen, cands))
        print(cands)

        print(min([s[l:r+1] for l,r in cands]))
        return min([s[l:r+1] for l,r in cands])