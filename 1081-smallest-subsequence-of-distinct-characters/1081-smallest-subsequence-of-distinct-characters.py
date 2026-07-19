class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        last = {}
        for i, c in enumerate(s):
            last[c] = i

        stack = []
        seen = set()

        for i, c in enumerate(s):
            if c in seen:
                continue

            while stack and stack[-1] > c and last[stack[-1]] > i:
                seen.remove(stack.pop())

            stack.append(c)
            seen.add(c)

        return "".join(stack)