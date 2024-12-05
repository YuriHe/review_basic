class Solution:
    """
    Question: Triplets
    SOLUTION1: three loops
    SOLUTION2: hashmap
    Counts frequency of each unique number
    iterate number of middle element b, and the number of left as a, right as c. This time, the number of triples that 
    meet a*b*c; then update a =a+b and continue to enumerate the number of middle element b
    Distinct triplet formation ensure all three elements from three groups, a, b, c
    """
    def unequalTriplets(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        n = len(nums)
        ans, a = 0, 0
        for b in cnt.values():
            c = n - a - b
            ans += a * b * c
            a += b
        return ans