class Solution:
    """
    Check pop element after meet
    1.negative go to left, positive go right
    2.size
    use stack when iterate array
    asteroids[i] != 0
    """
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for n in asteroids:            
            # handle collision
            while n < 0 and len(stack) > 0 and stack[-1] > 0:
                last = stack[-1]
                # larger negative
                if abs(n) > last:
                    stack.pop()
                # smaller negative, go to next asteroid
                elif abs(n) < last:
                    break
                # same size pop&next
                else:
                    stack.pop()
                    break
            else:
                # no collision
                stack.append(n)
        
        return stack


