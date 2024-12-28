# https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/#
"""
Tn = 2T(n/2) + (O(n) +nlogn + O(n))
Master theory
Tn = n logn logn
"""
import math

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def dist(p1, p2):
	return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


def divide(pointers, left, right): # logn
    cur_min_dis = float('inf')
    if left == right: # same pointer
        return cur_min_dis
    if left+1 == right: # two pointers
        return dist(pointers[left], pointers[right])
    # 1 step: devide two half
    mid = left+(right-left) // 2
    left_min_dis = divide(pointers, left, mid)
    right_min_dist = divide(pointers, mid, right)
    cur_min_dis = min(left_min_dis, right_min_dist)
    # 2 step assume 距离最近的两个点分别在左右分区中
    # Handle X first
    # Get the x-coordinate of the midpoint
    mid_x = pointers[mid].x

    # Initialize a list to hold points near the dividing line
    valid_Xpoints = []

    # Iterate through the points in the current range
    for point in pointers[left:right + 1]:
        # Check if the point is within cur_min_dis of the dividing line
        if abs(point.x - mid_x) < cur_min_dis:
            valid_Xpoints.append(point)

    # Handle Y
    valid_Xpoints.sort(key=lambda p: p.y)
    for i in range(len(valid_Xpoints)-1):
        for j in range(i+1, len(valid_Xpoints)):
            if valid_Xpoints[j].y - valid_Xpoints[i].y > cur_min_dis:
                break
            tempD = dist(valid_Xpoints[j],valid_Xpoints[i])
            cur_min_dis = min(tempD, cur_min_dis)
    return cur_min_dis


if __name__ == "__main__":
    pointN = 6
    pointX = [2,12,40,5,12,3]
    pointY =[3,30,50,1,10,4]
    points = [Point(x=x,y=y) for x, y in zip(pointX, pointY)]
    points.sort(key=lambda p: p.x)
    print("The smallest distance is", divide(points, 0, pointN-1))
