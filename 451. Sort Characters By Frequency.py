class Solution:
    """
    Question sort based on frequency
    """
    def frequencySort(self, s: str) -> str:
        # 1SOLUTION: counter + sort
        Counter dict 
        ctn = collections.Counter(s)
        # return [k, v]
        ls = sorted(ctn.items(), key=lambda x: -x[1])
        res = []
        for k,v in ls:
            res.append(k*v)
        return "".join(res)
        # 2SOLUTION: bucket sort
        bucket = [[] for _ in range(len(s)+1)]#create bucket size+1(freq)
        ctn = collections.Counter(s)
        for c, freq in ctn.items():
            bucket[freq].append(c)#freq as index, push char

        res = []
        for freq in range(len(bucket)-1, -1, -1):
            if bucket[freq]:
                for c in bucket[freq]:
                    res.append(c*freq)
        return "".join(res)
