from functools import cache
class Solution:
    """
    Question: return number of ways to decode string into valid char
    single digit decode to A to I
    two digits decode into J to Z
    any code starting with 0 is invalid
    """
    def numDecodings(self, s: str) -> int:
        """
        SOLUTION1: DFS / TopDOWN DP
        STEP: dp[i] means how many ways to decode s[0:i], each time when call dfs should valid digits
        """
        # pass value, number of ways
        dp = [0] * len(s)
        @cache
        def dfs(i):
            # base case 
            if i == len(s):
                return 1 # done one combination
            # invalid case, i as first one
            if s[i] == '0':
                return 0
            # first digit decoded
            count = dfs(i+1)
            # second digit decoded
            if i+1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
                count += dfs(i+2)
            return count
        return dfs(0)




