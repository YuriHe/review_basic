### Array
Insertion/deleteion: O(n)
Retrieve: O(1)

for fixed size of data, more retrieve but less insert/delete

### Linkedlist
Insertion/deleteion: O(1)
Retrieve: O(n)

for flexiable size of data, less retrieve but more insert/delete

### Heap
min heap(default, aka. PQ): smallest on top(also first out)

each max_heapify or min_heapify: O(logn)
build_maxheap or build_minheap: O(n)
heap_sort for all: O(nlogn)
Space: O(n)