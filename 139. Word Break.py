class Solution:
    """
    Question: Check if input s can be segmented into sequence of dictionary words which can be resused.
    Check if any combination of dictionary words can become input s. 
    Use Two pointer + bottom up DP, dp[cur] return true if cur string can get combination from dic words
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        SOLUTION1: bottom-top DP
        IDEA: create dp with size+1, consider dp[0] means emtpty string = true; 
        nested loop. fixed right index, to verify sub[0:left] and sub[left:right] if in dict
        dp[i] mean bool value of find word in dict ending at i index
        TIME: O(n*m*t) n is length of s, m is number of wordDict, t is maximum length of any words in wordDict
        """
        # size+1, dp[0] is empty string
        dp = [False] * (len(s)+1)
        dp[0] = True

        for right in range(1, len(dp)):
            for left in range(0, right): # not right+1 because 0 used first pos
                if dp[left] and s[left:right] in wordDict: # check substring index at right-1
                    dp[right] = True
                    break

        return dp[-1]

        """
        SOLUTION2: DFS hashset TLE
        use dfs recursively search input string s, to verify whole s can created by all words in Dict
        TIME: O(n*2^n + m)
        SPACE: O(n + (m+l))
        n is length of string s, m is number of wordDic, l is maximum length of any words in wordDic
        """
        dic = set(wordDict)

        def dfs(idx):
            # base case
            if idx == len(s):
                return True
            
            for right in range(idx, len(s)):
                if s[idx: right+1] in dic:
                    if dfs(right+1):
                        return True
            return False

        return dfs(0) # pass variable for dfs to verify if this path works


        