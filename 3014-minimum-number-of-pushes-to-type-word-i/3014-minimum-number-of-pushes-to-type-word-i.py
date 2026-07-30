class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)

        ans = 0
        push = 1

        for i in range(n):
            ans += push

            if (i + 1) % 8 == 0:
                push += 1

        return ans