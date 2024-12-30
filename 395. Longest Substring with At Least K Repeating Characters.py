class Solution:
    """
    return longest substring,eachchar occur >= k
    only 26 letters, can fix unqiuenumber and then sliding window
    unique: 1, maintain window is only unique 
    """
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0

        for unique_target in range(1,27,1): # [1,26]
            # intialize pointers, window, unique here since we try all 26 unique to find longest, between them is no relation
            window = collections.defaultdict(int)
            left, right = 0,0
            unique, at_least_k = 0, 0
            while right < len(s):
                cur = s[right]
                # 1.Variable check if this char is first time occur if yes, mark unique; latter occur won't count
                if window[cur] == 0:
                    unique += 1
                # 2.Add to window
                window[cur] += 1
                # 3.Variable Check cur chars occur first time meet >=k
                if window[cur] == k:
                    at_least_k += 1
                # shrink window 4.Invalid window
                while unique > unique_target:
                    leftchar = s[left]
                    # reset all the effects
                    if window[leftchar] == k: # not >= only count once
                        at_least_k -= 1
                    window[leftchar] -= 1
                    if window[leftchar] == 0:
                        unique -= 1
                    left += 1
                # 5.res
                if unique == unique_target and unique == at_least_k: # not >= eg.3unique should have 3 at_least_k
                    res = max(res, right-left+1)


                right += 1

        return res


