class Solution:
    """
    rearranging string in a zigzag pattern based on rownum
    1.edge case numRows=1
    2.use dict to store char for each row and concatenate all rows in the end
    3.use pointer p to control current row and use isDown to manage the direction of traversal
    """
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        dic = {}
        for i in range(1, numRows+1):
            dic[i] = ""
        p = 1
        isDown = True

        for c in s:
            dic[p] += c
            if p == 1 or (p < numRows and isDown):
                p += 1
                isDown = True
            else:
                p -= 1
                isDown = False

        return "".join(dic.values())
