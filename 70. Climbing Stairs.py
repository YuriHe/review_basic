"""
    Question: how many ways to climb to the top, choice is 1 step or 2steps
    Topic: DP Memorization
"""
def climbStairs(self, n: int) -> int:
    # create dp array with n+1 size, since need n steps/result
    dp = [0] * (n+1)
    # basic case NO USE dp[0], that is why dp size+1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    # assign val after can handle corner case
    dp[1], dp[2] = 1, 2
    for i in range(3, len(dp)):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]