class Solution:
    """
    Constraints:
    endWord must in list, but not startWord
    each transform, word will be in list and diff one letter 
    length of all word in list = beginword's length = endword's length
    all lowercase
    BFS
    q store word
    """
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        # create pattern dict store {pattern: [w1,w2]}
        wordList.append(beginWord)
        adj = collections.defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:] # *ot, h*t, ho*
                adj[pattern].append(word)
        
        # q find path
        q = deque([beginWord]) # q store word
        visit = set()
        visit.add(beginWord)
        step = 1
        while q:
            size = len(q)
            for _ in range(size):
                word = q.popleft()
                if word == endWord: return step
                for j in range(len(word)):
                    #search pattern based j
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in adj[pattern]: # search neigbhors
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)
            step+= 1

        return 0 # no found any path to reach endWord
