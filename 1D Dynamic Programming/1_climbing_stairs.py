class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n):
            temp = one + two
            two = one
            one = temp
        return one


s = Solution()
print(s.climbStairs(5))
