class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        # substring sliding window, when cur char not in dic and dic.size==k
        # move left 
        char = collections.defaultdict(int)
        res, left, right = 0,0,0

        while right < len(s):
            # update dic
            c = s[right]
            char[c] += 1

            # handle invalid window
            while len(char) > k:
                char[s[left]] -= 1
                if char[s[left]] <= 0:
                    # remove key
                    del char[s[left]]
                left += 1
            
            # update res
            res = max(res, right - left + 1)
            right += 1
        return res






