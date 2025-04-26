class Solution:
    """
    QUESTION: rotate string, cannot change order of characters
    """
    def rotateString(self, s: str, goal: str) -> bool:
        """
        SOLUTION1: string implement
        if verify string is rotated,check if s in goal+goal
        """
        return s in goal+goal and len(s) == len(goal)
        