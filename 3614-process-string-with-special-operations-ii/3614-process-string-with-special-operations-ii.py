class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        LIMIT = 10 ** 15 + 1

        n = len(s)
        length = [0] * (n + 1)

        for i, c in enumerate(s):
            cur = length[i]
            if 'a' <= c <= 'z':
                cur += 1
            elif c == '*':
                if cur:
                    cur -= 1
            elif c == '#':
                cur = min(cur * 2, LIMIT)
            else:  # '%'
                pass
            length[i + 1] = cur

        if k >= length[n]:
            return '.'

        for i in range(n - 1, -1, -1):
            c = s[i]
            cur = length[i + 1]
            prev = length[i]

            if 'a' <= c <= 'z':
                if k == prev:
                    return c
            elif c == '*':
                if cur < prev:
                    continue
                else:
                    if k == prev:
                        continue
            elif c == '#':
                half = prev
                if k >= half:
                    k -= half
            else:  # '%'
                if cur:
                    k = cur - 1 - k

        return '.'