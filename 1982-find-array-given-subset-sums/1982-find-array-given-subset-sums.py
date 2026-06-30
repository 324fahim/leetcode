from collections import Counter

class Solution(object):
    def recoverArray(self, n, sums):
        """
        :type n: int
        :type sums: List[int]
        :rtype: List[int]
        """
        def dfs(sums, n):
            if n == 0:
                return []

            sums.sort()
            x = sums[1] - sums[0]

            cnt = Counter(sums)
            left = []
            right = []

            for s in sums:
                if cnt[s] == 0:
                    continue
                cnt[s] -= 1
                cnt[s + x] -= 1
                left.append(s)
                right.append(s + x)

            if 0 in left:
                return dfs(left, n - 1) + [x]
            else:
                return dfs(right, n - 1) + [-x]

        return dfs(sums, n)