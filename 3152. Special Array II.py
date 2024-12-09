class Solution:
    """
    3152. Special Array II
    Brute force: N^2 TLE
    """
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # check subarray of each query, all adjacent element are in diff parity
        # each query find subarray, then compare neighbors, use isEven or not, exchange
        # 1 SOLUTION: TLE
        # res = [False] * len(queries)
        # part = [1 if n%2 == 0 else 0 for n in nums]

        # for i, query in enumerate(queries):
        #     start, end = query # included bound
        #     isSpecial = True
        #     for j in range(start, end):
        #         if part[j] == part[j+1]:
        #             isSpecial = False
            
        #     res[i] = isSpecial

        # return res


        n = len(nums)
        # Step 1: Track the start index of each "special segment"
        # get [0,1,...n-1]
        # Initialize: each element is its own segment
        special_start = list(range(n))  
        
        for i in range(1, n):
            if nums[i] % 2 != nums[i - 1] % 2:
                special_start[i] = special_start[i - 1]
        
        # Step 2: Answer each query
        result = []
        for from_idx, to_idx in queries:
            if special_start[to_idx] <= from_idx: # special range is earlier than from_idx
                is_special = True
            else:
                is_special = False
            result.append(is_special)
        
        return result
                

