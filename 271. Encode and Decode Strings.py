class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.

    Simply use delimiter won't work, since str may include any possible characters
    """
    def encode(self, strs):
        """
        Decode logic: 'LengthofWord# + originalWord'  # as delimiter 
        """
        res = ""
        for word in strs:
            l = len(word)
            res += str(l) + "#" + word
        return res

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        res = []
        i = 0
        while i < len(str):
            j = i # grab encode part
            while str[j] != "#":
                j += 1
            w_l = int(str[i:j])
            word = str[j+1:j+1+w_l] # careful pointer
            res.append(word)
            # update i
            i = j+1+w_l
        return res

        
