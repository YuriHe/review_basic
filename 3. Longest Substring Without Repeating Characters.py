class Solution:
    """
    Question: longest substring(consecutive) without repeating characters(ASCII 256)
    Sliding window
    1.arr store 256 char, see/kick +/-
    2.define l, r, use r to track whole string, l for shirnk window
    3.return max length of substring: r-l+1
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 3SOLUTION
        if len(s) == 0: return 0
        # create arr to store char's freq
        seen = [0] * 256
        # define left, right of window
        l, r = 0, 0
        res = 0

        # use r to track string
        while r < len(s):
            # add cur char, update seen
            seen[ord(s[r])] += 1

            # resize window if s[r] occur >=1 in cur substring
            while l <= r and seen[ord(s[r])] > 1:
                # remove left from seen
                seen[ord(s[l])] -= 1
                # move on left pointer
                l += 1
            
            # get max length of unique substring
            res = max(res, r-l+1)
            # move on right pointer
            r += 1
        
        return res

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1SOLUTION: hashmap, move left one by one
        # create hashmap store{char: ctn} within window
        hashmap = collections.defaultdict(int)
        res = 0
        # same direction two pointers
        left, right = 0, 0
        while right < len(s):
            # invalid window exit duplicate inside of window
            if s[right] in hashmap:
                left = max(hashmap[s[right]], left)
            # update hashmap index
            hashmap[s[right]] = right+1
            # valid 
            res = max(res, right-left + 1)
            right += 1
        return res
        # 2SOLUTION:hashset (best)
        visit = set()
        left=0
        res = 0
        for right in range(len(s)):
            c = s[right]
            # 1.出 check window and move left
            while c in visit:
                visit.remove(s[left])
                left += 1
            # 2.进 update
            visit.add(c)
            # 3.算 res
            res = max(res, right-left+1)

        return res