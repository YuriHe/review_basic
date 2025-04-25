class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words= re.sub(r'[^\w\s]', ' ',paragraph.lower()).split()
        # OR
        words = re.findall(r'\w+', paragraph.lower())
        banset = set(banned)
        ctn = defaultdict(int)
        for w in words:
            if w not in banset:
                ctn[w] += 1
        most_freq = max(ctn.values())
        for k, v in ctn.items():
            if v == most_freq:
                return k
        return ''