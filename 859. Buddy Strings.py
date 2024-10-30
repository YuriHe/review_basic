class Solution:
    """
    Question: Only swap two letters must one time and see if they are same
    TODO: 
    1.if s==goal, check Counter, if >= 2 mean can swap
    2.swapcount =? 2
    S: O(2n), T:O(n)
    """
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): 
            return False # cannot swap

        s_map = Counter(s)
        g_map = Counter(goal)
        swap_count = 0

        if s == goal:
            for i in range(len(s)):
                if s_map[s[i]] >= 2:
                    # freq>= 2 aa can swap
                    return True
            # no found duplicate can swap
            return False
        else:
            for i in range(len(s)):
                if s_map[s[i]] != g_map[s[i]] or swap_count > 2:
                    return False
                else:
                    if s[i] != goal[i]:
                        swap_count += 1
        return swap_count == 2


        
                
            




                        
