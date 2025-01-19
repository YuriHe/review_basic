### Traverse Gragh
997. Find the Town Judge
#### DFS
841. Keys and Rooms
#### BFS
fixed size of bfs and seach layer by layer
127. Word Ladder
934. Shortest Bridge
1091. Shortest Path in Binary Matrix
1926. Nearest Exit from Entrance in Maze


### Union find - Undirected graph - Disjoin Set
#### Template
When use: group direct/indrect connections
parent = [i for i in range(nodes)]
rank=[1]*nodelen
def find(node): return node. track root of tree and path compression
def union(n1, n2): return count. update parent and rank 

323. Number of Connected Components in an Undirected Graph


### Directed weighted graph
#### DFS
802. Find Eventual Safe States
1466. Reorder Routes to Make All Paths Lead to the City Zero
#### BFS
When use:
1.relation
2.shortest path 
Steps:
define queue
define visit
##### Template
```
# build graph
adj = defaultdict(list) # src: [des, val]
for i, v in enumerate(equations):
    src, des = v
    adj[src].append([des, values[i]])
    adj[des].append([src, 1/values[i]])

q=deque([])
q.append((src, 1)) # only tuple, not list in queue
visit=set()
visit.add(src)
while q:
cur,val = q.popleft()
for nei, weight in adj[cur]:
    if nei not in visit:
        q.append((nei, weight*val))
        visit.add(nei)
```

399. Evaluate Division
1129. Shortest Path with Alternating Colors
1376. Time Needed to Inform All Employees (directed tree, no cycle, no visit)


### What is graph
edge between i and j
node
directed or undirected
Time: O(E+V) or O(ElogV)


### Dijkstra's algorithm 
shortest path - greedy BFS - heap - T:O(ElogV)
499. The Maze ||
1368. Minimum Cost to Make at Least One Valid Path in a Grid
1514. Path with Maximum Probability (maxheap)
2290. Minimum Obstacle Removal to Reach Corner







### BFS
Need finding the shortest path on an unweighted graph, the fewest number of moves to reach the target.
1. 752.Open the Lock


