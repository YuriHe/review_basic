class Solution:
    """
    Question: verify if balanced parenthese after modify:total ( = total ) in the end, in process, ( count > )count
    """
    def canBeValid(self, s: str, locked: str) -> bool:
        # how know with which curly bracket as pair
        # Use stack: locked stack store ( index; unlocked stack store wildcat index 
        # when see ) first, check locked stack greedy
        # CX)X)XX). CXCXCXX)
        if len(s) % 2 != 0: return False # balanced string must even length not odd
        lock = []
        unlock = []
        for i in range(len(s)):
            if locked[i] == '0':
                unlock.append(i)
            elif s[i] == "(":
                    lock.append(i)
            else:
                if lock:
                    # greedy check locked stack
                    lock.pop()
                elif unlock:
                    unlock.pop()
                else:
                    return False
        # When many (
        while unlock and lock and lock[-1] < unlock[-1]:
            lock.pop()
            unlock.pop()
        return len(lock) == 0

              