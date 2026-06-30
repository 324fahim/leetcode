class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)

        if n > m:
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(m):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[j + 1] += dp[j]

        return dp[n]