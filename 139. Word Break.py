"""
    Question: Check if input s can be segmented into sequence of dictionary words which can be resused.
    Check if any combination of dictionary words can become input s. 
    Use Two pointer + bottom up DP, dp[cur] return true if cur string can get combination from dic words
"""
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    # define dp array. size+1, since dp[0]. "" always true
    dp = [False] * (len(s)+1)
    dp[0] = True
    
    for i in range(1, len(dp)): # right pointer, handle substring
        for j in range(0, i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
    return dp[-1]
