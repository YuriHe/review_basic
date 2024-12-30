### Binary Search
1D
See if O(logn) + sorted array -> Think binary search
If both mid+1 and mid-1, while left <= right; otherwise, left < right
2D 
sorted 2d array
rows =3, columns = 4
low = 0, high = m*n-1       eg.0, 3*4-1=11
mid = (low+high) // 2       eg.5
midrow = mid // columns     eg.1
midcol = mid % columns.     eg.1
##### template
1.
```
start=0,end=len-1
while start<=end:
    mid = (start+end)//2
    if nums[mid]<target:
        start =mid+1
    else:
        end =mid-1
//(end, start)
```
2.
```
left=0,right=len
while left<right:
    mid
    if nums[mid] < target:
        left=mid+1
    else:
        right=mid
//(left==right)
```

4. Median of Two Sorted Arrays
33. Search in Rotated Sorted Array
34. Find First and Last Position of Element in Sorted Array
35. Search Insert Position
69. Sqrt(x) # return right, since left<= right, right is math.floor
74. Search a 2D Matrix
153. Find Minimum in Rotated Sorted Array
162. Find Peak Element
278. First Bad Version
410. Split Array Largest Sum
704. Binary Search
875. Koko Eating Bananas
1011. Capacity To Ship Packages Within D Days
1482. Minimum Number of Days to Make m Bouquets
1552. Magnetic Force Between Two Balls
1760. Minimum Limit of Balls in a Bag
2141. Maximum Running Time of N Computers


### Sort+Binary search
15. 3Sum
436. Find Right Interval
2300. Successful Pairs of Spells and Potions


### Sliding Window
#### template
count = [0] * n
left, right = 0, 0
while right < arr:
    # update count += 1
    # handle invalid window
    if .... >:
        move left 
        decrement count
    # update valid res

3. Longest Substring Without Repeating Characters
76. Minimum Window Substring
209. Minimum Size Subarray Sum
340. Longest Substring with At Most K Distinct Characters
395. Longest Substring with At Least K Repeating Characters
424. Longest Repeating Character Replacement
643. Maximum Average Subarray I
1004. Max Consecutive Ones III  1493. Longest Subarray of 1's After Deleting One Element
1248. Count Number of Nice Subarrays
1456. Maximum Number of Vowels in a Substring of Given Length
2405. Optimal Partition of String
2779. Maximum Beauty of an Array After Applying Operation


### Modify in-place with (1) extra memory
26. Remove Duplicates from Sorted Array
27. Remove Element
80. Remove Duplicates from Sorted Array II
189. Rotate Array
283. Move Zeroes


### Linked list
#### Create linkedlist
2. Add Two Numbers
21. Merge Two Sorted Lists
148. Sort List
#### Iterate linkedlist
141. Linked List Cycle
142. Linked List Cycle II
2130. Maximum Twin Sum of a Linked List
#### Edit linkedlist
203. Remove Linked List Elements
206. Reverse Linked List
2095. Delete the Middle Node of a Linked List


### Consider Index 
11. Container With Most Water
121. Best Time to Buy and Sell Stock
122. Best Time to Buy and Sell Stock II


### 相向
16. 3Sum Closest



59. Spiral Matrix II
792. Number of Matching Subsequences
1351. Count Negative Numbers in a Sorted Matrix
