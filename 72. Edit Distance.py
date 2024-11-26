class Solution:
    """
    Question:
    count number of ways, choices are insert, delete, replace
    -> DFS with memorization
    change word1 to word2
    """
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and word2: return len(word2)
        if not word2 and word1: return len(word1)

        # set 2d memo
        # WHY: not 1D, since need to mark [i][j] two indexes from two strings and memorize their optimizal scene in cur state
        memo =[[0 for j in range(len(word1))] for i in range(len(word2))]

        def dfs(i, j):
            # base case MUST CHECK boundary first
            if i == len(word2):
                # no use memo, but use rest of word1
                return len(word1) - j
            if j == len(word1):
                return len(word2) - i
            
            # check if need to update memo
            if memo[i][j] > 0:
                return memo[i][j]
            
            if word1[j] == word2[i]:
                memo[i][j] = dfs(i+1, j+1)
            else:
                # choose insert to word1
                add = dfs(i+1, j)
                # choose delete to word1
                delete = dfs(i, j+1)
                # if choose replace
                replace = dfs(i+1, j+1)

                # compare which operation best at that point
                memo[i][j] = min(add, delete, replace) + 1
            return memo[i][j]

        
        return dfs(0, 0)

