from math import factorial

class Solution(object):
    def countGoodIntegers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i

        seen = set()
        ans = 0

        half = (n + 1) // 2
        start = 10 ** (half - 1)
        end = 10 ** half

        for first in range(start, end):
            s = str(first)

            if n % 2 == 0:
                pal = int(s + s[::-1])
            else:
                pal = int(s + s[-2::-1])

            if pal % k != 0:
                continue

            cnt = [0] * 10
            for ch in str(pal):
                cnt[ord(ch) - ord('0')] += 1

            key = tuple(cnt)
            if key in seen:
                continue
            seen.add(key)

            total = 0

            for first_digit in range(1, 10):
                if cnt[first_digit] == 0:
                    continue

                cnt[first_digit] -= 1

                ways = fact[n - 1]
                for c in cnt:
                    ways //= fact[c]

                total += ways
                cnt[first_digit] += 1

            ans += total

        return ans