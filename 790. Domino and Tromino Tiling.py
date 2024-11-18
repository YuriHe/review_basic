class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10** 9 + 7
        if n < 3:
            return n
        
        # set 2d array with extra row/column
        dp = [[0] * 3 for _ in range(n+1)]
        dp[0][0] = 1 # no tiles
        dp[1][0] = 1 # put 2*1 horizontally
        dp[1][1] = 1 # unfill top 1 and put 1* 2 in bottom
        dp[1][2] = 1 # unfil bottom 1 and put 1*2 in top

        for i in range(2, len(dp)):
            # full cover:vertical+horizontal+(take 2rows, extra1top) + (take 2rows, extra1bottom)
            dp[i][0] = (dp[i-1][0] + dp[i-2][0] + dp[i-2][1] + dp[i-2][2]) % MOD
            # extra 1 top
            dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD
            # extra 1 bottom
            dp[i][2] =(dp[i-1][0] + dp[i-1][1]) % MOD

        return dp[n][0]