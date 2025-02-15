class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        1.Solution: sliding window & hashset(Best)
        Idea:if repeat, move left pointer
        T:O(n), S: O(n)
        """
        # maintain window(unique)
        visit, left, resMax = set(), 0, 0
        for right in range(len(s)):
            # 1STEP: (MOVE LEFT) verify current already visited
            while s[right] in visit:
                visit.remove(s[left])
                left += 1
            # 2STEP: (ADD RIGHT) now push cur to visit
            visit.add(s[right])

            # 3STEP: (UPDATE RES)
            resMax = max(resMax, right-left+1)
        return resMax
        """
        2.Solution: sliding window&hashmap
        T:O(n), S: O(n)
        """
        # maintain window(frequency)
        window = collections.defaultdict(int)
        resMax, left = 0,0
        for right in range(len(s)):
            # 1STEP: (ADD RIGHT)
            window[s[right]] += 1
            # 2STEP: (MOVE LEFT) maintain window
            while window[s[right]] > 1: 
                window[s[left]] -= 1
                left += 1
            # 3STEP:(UPDATE RES)
            resMax = max(resMax, right-left+1)
        return resMax

