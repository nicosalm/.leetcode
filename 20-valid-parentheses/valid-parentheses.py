class Solution:
    def isValid(self, s: str) -> bool:
        # let's solve this with a stack and a dictionary
        stack = []
        dict = {"]":"[","}":"{",")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys(): # if matching DNE or is not adjacent, return false
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return True
        return stack == [] 