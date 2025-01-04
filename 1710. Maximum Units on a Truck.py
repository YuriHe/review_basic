class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # # 1SOLUTION: sort+greedy+nested loop
        res = 0
        # sort based on unit 
        boxTypes.sort(key=lambda x: -x[1])

        # used box 0 to truckSize or cur box
        used = 0
        for part in boxTypes:
            box = part[0]
            unit = part[1]
            cur = box
            while used < truckSize and cur > 0:
                res += unit
                cur -= 1
                used += 1
        return res

        # 2SOLUTION: sort+greedy+one pass
        res = 0
        # sort based on unit 
        boxTypes.sort(key=lambda x: -x[1])

        # used box 0 to truckSize or cur box
        used = 0
        for box, unit in boxTypes:
            if box < truckSize:
                res += box * unit
                truckSize -= box
            else:
                res += truckSize * unit
                return res
        return res