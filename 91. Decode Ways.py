# from functools import cache

def numDecodings(s):
# Question: number of ways to decode num string to char string
# DP top-bottom with memo=recursion two ways
    if not s or s[0] == "0": return 0
    
    memo = [0] * len(s)
    # @cache
    def dp(i):
        print(i, " ", memo) # in the end ,all will back to dp{0} memo[0]
        # base case
        if i == len(s):
            return 1
        if memo[i] > 0:
            return memo[i]
        if s[i] != '0':
            # single digit decode
            memo[i] += dp(i+1)
        if i+1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
            # two digits decode
            memo[i] += dp(i+2)
        return memo[i]

    return dp(0)

print(numDecodings("123"))