from functools import cache
class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = [None] * 26
        self.isEnd = False
class Trie:
    def __init__(self):
        # create Trie root
        self.root = TrieNode(-1)
    def add(self, word):
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                # add node
                cur.children[idx] = TrieNode(c)
            # move next level 
            cur = cur.children[idx]
        cur.isEnd = True
    def searchTwice(self, word, memo):
        if word in memo:
            return memo[word]
        @cache
        def dfs(index, node, count):
            # stop condition is finish iterating whole word
            if index == len(word):
                # at least two shorter words
                return count >= 2
            # start search trietree
            cur = node
            for i in range(index, len(word)):
                idx = ord(word[i]) - ord('a')
                if not cur.children[idx]:
                    return False
                cur = cur.children[idx]
                if cur.isEnd:
                    # found first shorter word, now start second dfs(start from root again)
                    if dfs(i+1, self.root, count+1):
                        return True
            # in the end 
            return False
            
        memo[word] = dfs(0, self.root, 0)
        return memo[word]

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # Question:find all words that combine >=2 shorter words from input
        # Topic: Trie and DFS find >=2 shorter
        # 1.create trienode, add all word from words
        trie = Trie()
        for word in words:
            trie.add(word)
        # 2.search if match push to res
        res = []
        # TLE without memo and cache
        memo = {}
        for word in words:
            if trie.searchTwice(word, memo):
                res.append(word)
        return res


