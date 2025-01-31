class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        1.Solution:hashmap+sort
        Idea: descend sort, but lexi order
        Time: O(nlogn)
        """
        ctn = Counter(words)
        sorted_t_ls = sorted(ctn.items(), key=lambda x: (-x[1], x[0])) # freq desc,word asc
        res = []
        for i in range(k):# k in range[1, len(sorted_t_ls)], wont overflow
            res.append(sorted_t_ls[i][0])
        return res
        """
        2.Solution:hashmap+heap
        Idea: descend sort, but lexi order,result need freq hightest to lower-> maxheap
        Time: O(nlogk)
        """
        ctn = Counter(words)
        maxheap = []
        for w, freq in ctn.items():
            heapq.heappush(maxheap, (-freq, w))
        res = []
        for _ in range(k):
            _, w = heapq.heappop(maxheap)
            res.append(w)
        return res