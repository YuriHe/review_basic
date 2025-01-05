class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # 1SOLUTION:TLE
        ls = list(s)
        for start, end, di in shifts:
            i = start
            while i <= end:
                if di == 1:
                    if ls[i] == "z":
                        ls[i] = "a"
                    else:
                        ls[i] = chr(ord(ls[i])+1)
                else:
                    if ls[i] == "a":
                        ls[i] = "z"
                    else:
                        ls[i] = chr(ord(ls[i])-1)
                i+=1
        return "".join(ls)
        # 2SOLUTION prefix sum
        """
        Question: modify string after shift changes
        Step1: create shift array mark start,end point shift changes, size n+1, we need [start, end], so drop end+1 wont affect cumulative shift
        Step2: handle shift changes for every index
        AB [[0,1,1],[0,1,0]] => BC-> AB no change!
        [0]+1,[1]-1-> [0]-1,[1]+1 no change!
        """
        shift = [0] * (len(s)+1)
        for start, end, di in shifts:
            di = 1 if di == 1 else -1
            shift[start] += di
            shift[end+1] -= di
        
        cumulative_shift = 0 # since need substring[start, end] with shift change
        res = []
        for i, char in enumerate(s):
            cumulative_shift += shift[i]
            
            newC = chr((ord(char) - ord('a') + cumulative_shift) % 26 + ord('a')) # make sure accu part [0, 25]
            res.append(newC)
        return ''.join(res)


