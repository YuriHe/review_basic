"""
    Question: Top k frequent words in list
    Solution1: Couter hashmap, sort T:O(nlogn) S:O(n)
"""
def topKFrequent(self, words: List[str], k: int) -> List[str]:
    word_freq = Counter(words)
    res = []

    # Sort the dictionary based on frequency, then lexicographically if the frequencies are the same
    freq_sorted_dict: List = sorted(word_freq.items(), key=lambda x: (-x[1], x[0]))
    for key, val in freq_sorted_dict:
        if k > 0:
            res.append(key)
            k -= 1
        else:
            break
    return res
