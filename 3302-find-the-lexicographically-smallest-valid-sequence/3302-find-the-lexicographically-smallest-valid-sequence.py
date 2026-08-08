class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """

        n = len(word1)
        m = len(word2)

        # last[j] = position of word2[j] in the
        # rightmost possible exact subsequence.
        last = [-1] * m

        i = n - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1

        ans = [0] * m

        j = 0
        can_mismatch = True

        for i in range(n):
            if j == m:
                break

            # Exact match: always prefer it.
            if word1[i] == word2[j]:
                ans[j] = i
                j += 1

            # Use this character as the one allowed mismatch.
            elif can_mismatch:
                # There must be enough room to match
                # word2[j+1:] exactly after i.
                if j == m - 1 or i < last[j + 1]:
                    ans[j] = i
                    j += 1
                    can_mismatch = False

        if j == m:
            return ans

        return []