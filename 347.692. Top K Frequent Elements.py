class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # can use builtin Counter as well
        ctn = {}
        for n in nums:
            ctn[n] = ctn.get(n, 0) + 1
        # ctn = Counter(nums)
        
        # 2 STEP create array store tuple(v, key) and sort array
        arr = []
        for key, v in ctn.items():
            arr.append([v, key])
        arr.sort(key=lambda x: x[0])

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

        # 2 STEP:
        # sort dic
        sorted_ls = sorted(ctn.items(), key=lambda x: -x[1])
        res = []
        for key, v in sorted_ls:
            res.append(key)
            if len(res) == k:
                return res
        return res

        
class Solution:
    """
    692. Top K Frequent Words
    Question: find top frequency
    1.count key's freq
    2.return res from highest to lowest, if same freq, base on lexicographical order
    """
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ctn = collections.Counter(words)
        
        # sort dict decreasing then lexicographical order
        sorted_ls = sorted(ctn.items(), key=lambda x: (-x[1], x[0]))

        res = []
        for key, v in sorted_ls:
            res.append(key)
            if len(res) == k:
                return res
        return []
