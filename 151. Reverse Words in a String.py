class Solution:
    def reverseWords(self, s: str) -> str:
        # remove all extra space in s
        arr = s.split() # convert s to list
        self.swap(0, len(arr)-1, arr)
        return " ".join(arr) # convert list to str


    def swap(self, start, end, arr):
        # swap arr in-place
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1


        