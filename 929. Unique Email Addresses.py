class Solution:
    """
    QUESTION:return number different email list that ignore all . in localname and all rest after '+'
    """
    def numUniqueEmails(self, emails: List[str]) -> int:
        """
        SOLUTION1: handle string
        """
        res = set()
        for e in emails:
            names = e.split("@")
            local=names[0]
            if '+' in local:
                idx=local.index('+')
                local=local[:idx]
            local=re.sub(r"\.", '', local)
            res.add(local+'@'+names[1])
        print(res)
        return len(res)
        