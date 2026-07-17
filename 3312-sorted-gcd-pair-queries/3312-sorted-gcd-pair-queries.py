from bisect import bisect_right

class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        cnt = [0] * (mx + 1)

        # cnt[g] = numbers divisible by g
        for g in range(1, mx + 1):
            s = 0
            for j in range(g, mx + 1, g):
                s += freq[j]
            cnt[g] = s

        # exact[g] = number of pairs whose gcd is exactly g
        exact = [0] * (mx + 1)

        for g in range(mx, 0, -1):
            c = cnt[g]
            pairs = c * (c - 1) // 2

            j = g * 2
            while j <= mx:
                pairs -= exact[j]
                j += g

            exact[g] = pairs

        prefix = []
        vals = []
        cur = 0
        for g in range(1, mx + 1):
            if exact[g]:
                cur += exact[g]
                prefix.append(cur)
                vals.append(g)

        ans = []
        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(vals[idx])

        return ans