class Solution:
    """
    rearranging string in a zigzag pattern based on rownum
    1.edge case numRows=1
    2.use dict to store char for each row and concatenate all rows in the end
    3.use pointer p to control current row and use isDown to manage the direction of traversal
    """
    def convert(self, s: str, numRows: int) -> str:
        # control direction, within range, use bool isDown, pointer p+=1, -=1 go down or up
        if numRows == 1 or len(s) <=numRows: return s
        
        rows =[""] * (numRows+1) # store string for each rows
        p = 1
        isDown = True
        for i in range(len(s)):
            rows[p] += s[i]
            # control direction
            if p == 1:
                isDown = True
            elif p == numRows:
                isDown = False
            # move up or down
            if isDown:
                p += 1
            else:
                p -= 1
        return "".join(rows[1:])