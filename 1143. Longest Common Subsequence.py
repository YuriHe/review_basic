class Solution:
    """
    Question: longest common subsequence compare two strings
    2D array DP : https://www.youtube.com/watch?v=Ua0GhsJSlWM
    bottom up DP, O(n * m) from left bottom to top left
    same character go to diagnoal line
    diff character go to right or bottom
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # let text1 as column, text2 as row
        dp = [[0 for j in range(len(text2) +1 )] for i in range(len(text1) + 1)]

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                     dp[i][j] = 1 + (dp[i+1][j+1])
                else:
                     dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return dp[0][0]