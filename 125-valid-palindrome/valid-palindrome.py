class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = [c.lower() for c in s if c.isalnum()]
        return all (s[i] == s[~i] for i in range(len(s) // 2))

        
        # left, right = 0, len(s) - 1
        # s = s.lower()

        # while left < right:
            # while not s[left].isalnum() and left < right: left += 1
            # while not s[right].isalnum() and left < right: right -= 1

            # if s[left] != s[right]: return False
            # else:
                # left += 1
                # right -= 1

        # return True