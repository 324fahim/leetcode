class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        length = len(n)
        num = int(n)

        candidates = set()

        candidates.add(10 ** (length - 1) - 1)
        candidates.add(10 ** length + 1)

        prefix = int(n[:(length + 1) // 2])

        for p in (prefix - 1, prefix, prefix + 1):
            s = str(p)

            if length % 2 == 0:
                pal = int(s + s[::-1])
            else:
                pal = int(s + s[-2::-1])

            candidates.add(pal)

        candidates.discard(num)

        ans = None

        for x in candidates:
            if ans is None:
                ans = x
            elif abs(x - num) < abs(ans - num):
                ans = x
            elif abs(x - num) == abs(ans - num) and x < ans:
                ans = x

        return str(ans)