class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """
        SOLUTION1: sliding window
        within window, k - count(black) = op times
        assumption: k <= n
        """
        b_count = 0
        left = 0
        p = 0
        res = float("inf")

        for right in range(len(blocks)):
            if blocks[right] == "B":
                b_count += 1

            if right - left + 1 == k:
                # move left for next right
                ope = k-b_count
                res = min(res, ope)
                if res == 0:
                    return res
                # move left
                if blocks[left] == "B":
                    b_count -= 1
                left += 1

        return res

