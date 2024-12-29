class Solution:
    """
    find minimum substring from s, which include all characters in t
    """
    def minWindow(self, s: str, t: str) -> str:
        # create window hashmap 
        window = collections.defaultdict(int)
        t_count = collections.Counter(t)
        left, right = 0,0
        matchC = 0
        minstart, minend = 0, float('inf')
        while right < len(s):
            char = s[right]
            # 1.进，add char to window
            window[char] += 1

            # 2.算 Check if found characters meet requirement(freq)within window
            if char in t and window[char] == t_count[char]:
                matchC += 1
            
            # 3.出 Valid window and shrink
            while left <= right and matchC == len(t_count):
                # if find another smaller valid window
                if right - left < minend - minstart:
                    minstart, minend = left, right
                
                # remove left char
                leftchar = s[left]
                window[leftchar] -= 1
                if leftchar in t_count and window[leftchar] < t_count[leftchar]: # affect valid res
                    matchC -= 1
                left += 1

            right += 1

        return s[minstart: minend+1] if minend != float('inf') else ""