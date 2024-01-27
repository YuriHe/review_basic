"""
    Question: check if subsequence
    Topic: subsequence VS. substring(consecutive)
    TODO: iterate s and t same time, return if t can reach the end
"""
def isSubsequence(self, s: str, t: str) -> bool:
    if len(s) > len(t): return False
    i_s = 0
    i_t = 0
    while i_s < len(s) and i_t < len(t): # if done s iterate, just out 
        if s[i_s] == t[i_t]:
            # find one char
            i_s += 1
            i_t += 1
        else:
            # not found, go to next one in t
            i_t += 1
    return i_s == len(s) # check if iterate whole s 