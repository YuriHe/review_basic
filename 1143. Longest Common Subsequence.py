class Solution:
    """
    Question: longest common subsequence compare two strings
    2D array 
    1.if character match, +1 
    2.if not match, max(text1 move 1 more, text2 move 2 more)
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        SOLUTION1: bottom up DP
        dp[i][j] means longest subseq 
        reverse thinking
        TIME SPACE O(n*m)
        """
        n, m = len(text1), len(text2)
        # create 2D dp col,row+1 since handle one of string is empty string
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        # fill out 2d dp table
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if text1[i] == text2[j]:
                    # grab diagnal value reverse thinking aa,ae 
                    dp[i][j] = 1+dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
