### Array
#### Complexity
Insertion/deleteion: O(n)
Retrieve: O(1)
for fixed size of data, more retrieve but less insert/delete

### Set
#### Time Complexity
Lookup/add/remove: O(1)

### Linkedlist
#### Complexity
Insertion/deleteion: O(1)
Retrieve: O(n)
for flexiable size of data, less retrieve but more insert/delete


### Heap
#### Complexity
each max_heapify or min_heapify: O(logn) or O(logk)
build_maxheap or build_minheap: O(n)
heap_sort for all: O(nlogk)
Space: O(n)
#### Usage
certain K slot
Minheap(PQ), smallest on top(first out)
kth smallest/largest
#### Structure
import heapq
heap = [-x for x in ls](maxheap, if minheap use x)
heapq.heapify(heap)
heapq.heappush(heap, v)
heapq.heappop(heap)


### Hashmap
#### Complexity
S:O(n)
T:O(1) for retrieve/append/remove
store k,v 
dic = defaultdic(list/int/set)


### Queue
#### Complexity
S: O(n)
T: O(1): append, popleft
q = deque([])
q.append((tuple/any))
q.popleft()
#### Usage
BFS


### Graph
#### Recursion 
Need visit, @cache, memo={}
find shortest path: bfs
find all combination: dfs


### DP
Ask optimal solution, overlap subprolem, combination/minimum/maximum
#### 1DP/2DP
top-bottom, dfs, memo, @cache, dfs(0):return memo
bottom-top, dp[-1], dp[i-1], dp[i-2], handle base case and transfer function

