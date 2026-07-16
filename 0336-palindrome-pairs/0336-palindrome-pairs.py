class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def isPal(s):
            return s == s[::-1]

        wordMap = {}
        for i, w in enumerate(words):
            wordMap[w] = i

        res = []

        for i, word in enumerate(words):
            m = len(word)

            for j in range(m + 1):
                left = word[:j]
                right = word[j:]

                # Left part is palindrome
                if isPal(left):
                    rev = right[::-1]
                    if rev in wordMap and wordMap[rev] != i:
                        res.append([wordMap[rev], i])

                # Right part is palindrome
                # j != m avoids duplicates
                if j != m and isPal(right):
                    rev = left[::-1]
                    if rev in wordMap and wordMap[rev] != i:
                        res.append([i, wordMap[rev]])

        return res