"""
Anagram swap + combination
"""
from itertools import product
from collections import *

def generate_sentences(wordSet, sentence):
    # use anagram dict {sortedW: [originalWs]}
    dic = defaultdict(list)
    for w in wordSet:
        s_w = "".join(sorted(w))
        dic[s_w].append(w)
    
    # handle sentence str to array, and present by [[anagramgroup], [anagramgroup], [anagramgroup]]  anagramgroup can be same. for do Catesian product
    arr = sentence.split(' ')
    group = [] # order same as sentence
    for w in arr:
        key = "".join(sorted(w))
        if key in dic:
            group.append(dic[key])
        else:
            print("this word in sentence not include in WordSet")
    # product, list comprehension, convert to str
    res = [" ".join(combination) for combination in product(*group)]
    return res

# Test out
wordSet = ["listen", "silent", "it", "judy", "ujdy", "is"]
sentence = "listen it is silent"
result = generate_sentences(wordSet, sentence)
print(f"Count: {len(result)}")
print("Sentences:")
for sent in result:
    print(sent)
