class Trie:
    def __init__(self):
        self.children = {} #single folder string(no/):Trie
        self.endfolder = False

    def add(self, path) -> None:
        cur = self
        folder_ls = path.split("/")
        for f in folder_ls:
            if f not in cur.children:
                cur.children[f] = Trie()
            cur = cur.children[f]
        cur.endfolder = True

    def search(self, path) -> bool:
        cur = self
        # only need to search except last single folder
        folder_ls = path.split("/")
        for i in range(len(folder_ls)):
            if cur.endfolder:
                return True
            cur = cur.children[folder_ls[i]]
        return False
    

class Solution:
    """
        Question: Remove all sub-folders if exist
        HOW: /ab/c /ab/d -> no sub-folders, if have sub-folders definitely have more /s, can iterate folder name, use set to check if prev dir exist or not
    """
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # SOLUTION 1 brute force: hashset, O(n*L*Lslice)
        hash_set = set(folder)
        res = []

        for f in folder:
            res.append(f)
            for i in range(len(f)):
                if f[i] == "/" and f[:i] in hash_set:
                    res.pop()
                    break
        return res

        # SOLUTION2 Tree trie, O(n*L)
        trie = Trie()
        for f in folder:
            trie.add(f)

        res = []
        for f in folder:
            if not trie.search(f):
                res.append(f)
        return res





        