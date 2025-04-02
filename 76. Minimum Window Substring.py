class Solution:
    """
    Question: return shortest substring of s have all characters in t(order no matter)
    """
    def minWindow(self, s: str, t: str) -> str:
        """
        SOLUTION1: sliding window -> substring
        t allows duplicates, res must contains all in t => think hashmap store t
        STEP: 
        1.create two hashmap store t freq, window freq
        2.when start flexible-size window => no need to wait character appear in t, use another minstart, minend to follow
        3.when move left pointer => matchC = len(t), find another shorter substring
        """           
        tMap = collections.Counter(t)
        wMap = collections.defaultdict(int)
        minstart, minend = 0, float('inf')
        matchT, left = 0, 0

        for right in range(len(s)):
            cur = s[right]

            # 1step push into window
            wMap[cur] += 1

            # 2step check if char and all freq in T
            if cur in t and wMap[cur] == tMap[cur]:
                matchT += 1 # mean found this char and its all freq in window
            
            # 3step now already valid window see if shrink window size
            while left <= right and matchT == len(tMap):
                # update left, right find shorter valid substring
                if right -left < minend - minstart:
                    minstart, minend = left, right
                
                # move left pointer
                wMap[s[left]] -= 1
                # check if this action affect res
                if s[left] in tMap and wMap[s[left]] < tMap[s[left]]:
                    matchT -= 1
                left += 1
        return s[minstart: minend+1] if minend != float('inf') else ""


