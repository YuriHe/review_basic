class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        leftCount, rightCount, leftCost, rightCost = 0,0,0,0
        res = [0] * len(boxes)
        # handle left prefixsum
        for i in range(1, len(boxes)):
            if boxes[i-1] == '1':
                leftCount += 1
            leftCost += leftCount
            res[i] = leftCost
        for i in range(len(boxes)-2, -1, -1):
            if boxes[i+1] == "1":
                rightCount += 1
            rightCost += rightCount
            res[i] += rightCost
        return res 

