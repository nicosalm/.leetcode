class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        
        result = ''
        for string in strs:
            result += str(len(string)) + "$" + string
        print(result)
        return result
    
    
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        result = []
        i = 0
        while i < len(s):
            p = s.find('$', i) # locate $ in string
            length = int(s[i:p]) # assess length of each string as from i to $
            result.append(s[p+1:p+1+length]) # add the word to the list
            i = p+1+length # move past the pointer on to the next word
        return result


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))