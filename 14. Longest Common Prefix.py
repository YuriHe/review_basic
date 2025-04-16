class Solution:
    """
    QUESTION: find longest common prefix for whole list of string
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        SOLUTION1: traverse string and update flag in loop
        """
        flag = strs[0]
        for i in range(1,len(strs)):
            cur = strs[i]
            # two pointer to track flag and cur, if found diff then stop
            # choose min length from flag and cur string
            minL = min(len(flag), len(cur))
            p = 0
            tmp = ""
            while p< minL and flag[p]==cur[p]:
                tmp += flag[p]
                p+=1
                
            if len(tmp) == 0: # find one no command prefix exit earlier
                return ""
            else:
                flag = tmp
        return flag
        
        """
        SOLUTION2: traverse string and update flag after loop
        """
        flag = strs[0]
        for i in range(1,len(strs)):
            cur = strs[i]
            minL = min(len(flag), len(cur))
            p = 0
            while p< minL and flag[p]==cur[p]:
                p+=1
            flag = flag[:p] 
            if len(flag) == 0: # find one no command prefix exit earlier
                return ""
        return flag
            
            
                
