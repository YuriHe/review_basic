class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # create map for list1 {str:index}, str all unique
        # iterate list2 if find key in map, that check glo_idx if smaller update
        res = []
        idx = 2001 # at least one common string
        m1 = {}
        for i, s in enumerate(list1):
            m1[s]=i
        for i, s in enumerate(list2):
            if s in m1:
                if i+m1[s]<idx:
                    res = [s]
                    idx = i+m1[s]
                elif i+m1[s] == idx:
                    res.append(s)
        return res

        