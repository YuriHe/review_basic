class Solution:
    """
    Question: sweepline question -> interval/overlap, return merged [x,y] sorted by x
    the result is mean height changes
    eg. [[0,2,3],[2,5,3]],  building same hight, if not decreasing height will -3, 3
    """
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # create points 2d: [[start1, height1], [end1, -height1]]
        res = []
        points = []
        for b in buildings:
            points.append([b[0], b[2]]) # take off
            points.append([b[1], -b[2]]) # land
        # sort points based on [0],height negative first(start)
        points.sort(key=lambda x: (x[0], -x[1]))

        # maxheap store start building of height(negative)
        maxheap = [0]
        prev_height = 0
        # iterate points and push dynamically
        for p, h in points:
            if h > 0: # start build, push to heap from highests to lowest
                heapq.heappush(maxheap, -h)
            else: # end build
                # !!! remove corresponding START height, not pop
                maxheap.remove(h)
                heapq.heapify(maxheap)
            
            # current max height
            cur_height = -maxheap[0]
            # change height change
            if cur_height != prev_height:
                res.append([p, cur_height])
                prev_height = cur_height
        return res
