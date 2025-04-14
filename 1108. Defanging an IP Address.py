import re

class Solution:
    """
    QUESTION: replace all . with [.]
    """
    def defangIPaddr(self, address: str) -> str:
        """
        SOLUTION1: regular expression
        """

        s = re.sub(r"\.", "[.]", address)
        return s
        