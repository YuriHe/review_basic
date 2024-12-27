class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # maximum result of sum
        # 1SOLUTION: brute force n^2 
        # 2SOLUTION: one pass
        # vi+vj+i-j= (vi+i)+(vj-j), use maxI track vi+i
        res = 0
        max_i = values[0] #values[i]+0
        for j in range(1, len(values)): # i< j
            # Calculate the score for the pair (i, j) where max_i is the best prior i
            res = max(res, max_i + values[j]-j)
            # updat max_i for next iteration
            max_i = max(max_i, values[j]+j)
        return res
        
        
