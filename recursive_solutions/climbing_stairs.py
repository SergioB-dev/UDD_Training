class Solution:
    def climbStairs(self, n: int, memoize={1: 1, 0: 1}) -> int:
        if n in memoize:
            return memoize[n]
        else:
            memoize[n] = self.climbStairs(n-1, memoize) + self.climbStairs(n-2, memoize)
            return memoize[n]
