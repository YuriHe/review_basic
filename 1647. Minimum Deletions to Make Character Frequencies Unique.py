class Solution:
    """
    min Deletion
    """
    def minDeletions(self, s: str) -> int:
        res = 0
        count = collections.defaultdict(int)
        for char in s:
            count[char] += 1
        visit = set()

        for char, freq in count.items():
            while freq > 0 and freq in visit:
                res += 1
            # new freq will store to visit, no need to update count dictionary
            visit.add(freq)
        return res