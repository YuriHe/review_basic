class Solution:
    """
    Question: return length of longest palindrome subsequence
    consider longest common seq
    palindrome=> origin string = reversed string 
    => text1, text2(which reversed text1) see longest common seq
    # 1143
    """
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        SOLUTION1: bottom up 2DDP
        """
        s1 = "".join(reversed(s))
        n = len(s)

        dp =[[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == s1[j]:
                    dp[i][j] = 1+dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]

    