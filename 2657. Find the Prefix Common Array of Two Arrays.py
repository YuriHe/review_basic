class Solution:
    """
    Question:retrun list of prefix common count
    1.A,B is permutation of 1 to n(means num is unique)
    """
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # 1SOLUTION: intersection T: O(n^2) S: O(n)
        res = []
        for i in range(len(A)):
            # substract subarray[0:i]
            prefixA = A[:i+1] # include i
            prefixB = B[:i+1]
            # use intersection
            ctn_command = len(set(prefixA) & set(prefixB))
            res.append(ctn_command)
        return res
        # 2SOLUTION:greedy counting T: (n) S: O(n)
        # unseen =0, seenAorB =1, seenA&B=2
        seen = [0] * (len(A)+1) # since num[1:n] for tracking seen from both A,B
        count = 0
        idx = 0
        res = [0] * len(A)

        for a, b in zip(A, B):
            seen[a] += 1
            seen[b] += 1
            if seen[a] == 2:
                count += 1
            if a!=b and seen[b] == 2:
                count += 1
            res[idx] = count
            idx += 1
        return res
            





