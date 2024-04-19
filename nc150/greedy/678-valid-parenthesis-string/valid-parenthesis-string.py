class Solution:
    def checkValidString(self, s: str) -> bool:
        count_open = 0
        count_closed = 0
        length = len(s) - 1

        # traverse string from both ends
        for i in range(len(s)):

            # open parenthesis or asterisks
            if s[i] == '(' or s[i] == '*':
                count_open += 1
            else:
                count_open -= 1

            # closed parenthesis or asterisks
            if s[length - i] == ')' or s[length - i] == '*':
                count_closed += 1
            else:
                count_closed -= 1

            # counts go negative => invalid string
            if count_open < 0 or count_closed < 0:
                return False

        return True

        '''
        Notes:
        - Could also be a DP problem
        - O(n), O(1) Space
        '''
            