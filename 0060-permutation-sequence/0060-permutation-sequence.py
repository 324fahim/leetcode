import math

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [str(i) for i in range(1, n + 1)]
        k -= 1
        ans = []

        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            idx = k // fact
            ans.append(nums.pop(idx))
            k %= fact

        return "".join(ans)