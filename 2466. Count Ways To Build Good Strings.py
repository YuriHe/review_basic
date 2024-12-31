class Solution:
    """
    Return number of diff strings match patterns
    How many good string of length i  - zero / or one
    solution is larger value of i based on smaller value
    """
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD= 10 ** 9 + 7
        # create dp dp[i] means number of good string ending at this i length
        # need value from high
        dp = [0] * (high+1)
        # intial value of dp, one way o build empty string ""
        dp[0] = 1

        for i in range(1, high+1): # [1:high]
            if i >= zero: # can make up by zero now
                # append based on previous with zero result
                dp[i] += dp[i-zero]
            if i >= one:
                dp[i] += dp[i-one]
            # modulo
            dp[i] %= MOD
        # Only need length from [low, high]
        return sum(dp[low: high+1]) % MOD
