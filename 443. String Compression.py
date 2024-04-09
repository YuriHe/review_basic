class Solution:
    """
    Question: convert to char[freq] for consecutive chars. 
    ISSUE: modify input array instead of create new array + track left pointer
    TOPIC: use S:(1) Two pointer
    """
    def compress(self, chars: List[str]) -> int:
        # first char 
        count = 1
        # track result len
        self.left = 1 
        # keep update flag
        flag = chars[0]

        # helper , if use % / need to reverse, so just use string type
        def append_count(count):
            if count > 1:
                for c in str(count):
                    chars[self.left] = c
                    self.left += 1
                    
        for i in range(1, len(chars)):
            if chars[i] == flag: # same group
                count += 1
            else:
                # handle prev group
                append_count(count)
                # start new group
                count = 1
                # update flag
                flag = chars[i]
                # modify val in list
                chars[self.left] = flag
                # jump cur char's next index which for freq
                self.left += 1 
        
        # last group
        append_count(count)
        return self.left



        