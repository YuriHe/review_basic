class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        1.Solution: Sort+hashmap {tuple(sortedW): [w1, w2]}
        Time: (n*klogk) Space:n*k. n is number of string, k is length of the longest string
        """
        dic = defaultdict(list)
        for w in strs:
            sortedW = tuple(sorted(w))
            dic[sortedW].append(w)
        return list(dic.values())
        """
        2.Solution: hashmap {tuple(26CharCtnList): [w1, w2]}
        Time: (n*k), Space:(n)
        """
        res = defaultdict(list)
        for w in strs:
            charCtn = [0] * 26
            for c in w:
                key = ord(c) -ord('a')
                charCtn[key] += 1
            res[tuple(charCtn)].append(w)

        return list(res.values())
