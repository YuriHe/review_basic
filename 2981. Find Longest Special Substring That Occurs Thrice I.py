class Solution:
    """
    Find longest special substring occur at least three times
    special substring means only one single character
    binary search:
    if length x is valid special substring, then all length < x's substring also special
    -> binary search
    """
    def maximumLength(self, s: str) -> int:
        # 1SOLUTION: BRUTE FORCE (n^2) PASS
        res = -1
        substr_ctn = collections.defaultdict(int)

        def is_special(substring):
            return len(set(substring)) == 1

        # generate all substring
        for l in range(len(s)):
            for r in range(l+1, len(s)+1):
                substr = s[l:r]
                if is_special(substr):
                    substr_ctn[substr] += 1
        
        # find valid substring occur thrice
        for sub, ctn in substr_ctn.items():
            if ctn >= 3:
                res = max(res, len(sub))
        return res

        # 2SOLUTION: binary search
        def is_special(substring):
            return len(set(substring)) == 1
        
        def is_special_based_length(length):
            # check if is special substring of given length, which occur >=3 times
            # generate all substrings with length with all index
            ctn = collections.defaultdict(int) # store{sub: freq}
            for i in range(len(s) - length+1):
                sub = s[i: i+length]
                if is_special(sub):
                    ctn[sub] += 1
                    if ctn[sub] >= 3:
                        return True
            return False


        l, r = 1, len(s) # it is length, not index
        res = -1
        while l <= r:
            mid = (l + r) // 2
            if is_special_based_length(mid):
               # valid, so go further
               res = mid
               l = mid + 1
            else:
                r = mid - 1
        return res
