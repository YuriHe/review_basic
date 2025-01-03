class Solution:
"""
Question:rangeSum of head/tail of string
Step1:create check_ls for head/tail+1, else0; fill out prefixsum_ls
Step2:prefix[end]-prefix[start-1]=range sum
"""
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # prehandle 
        # vowels = ["a", "e", "i", "o",  "u"]
        vowels = set("aeiou")
        # check words list head and tail if vowels, if valid 1, else 0 for using prefix
        check =[1 if word[0] in vowels and word[-1] in vowels else 0 for word in words]
        res = [0] * len(queries)
        # prefix[j]-prefix[i]=subarray sum
        # fill out prefix array prefix template
        prefix = [0] * (len(words)+1)
        prefix[0] = check[0]
        for i in range(1, len(words)):
            prefix[i] = prefix[i-1] + check[i]

        for i, query in enumerate(queries):
            start = query[0]
            end = query[1]
            res[i] = prefix[end] - prefix[start-1] if start > 0 else prefix[end]
        return res

