class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        cnt = [0] * 26
        for ch in letters:
            cnt[ord(ch) - ord('a')] += 1

        n = len(words)

        # Precompute letter counts and score for each word
        wordCnt = []
        wordScore = []

        for word in words:
            c = [0] * 26
            s = 0
            for ch in word:
                idx = ord(ch) - ord('a')
                c[idx] += 1
                s += score[idx]
            wordCnt.append(c)
            wordScore.append(s)

        def dfs(i):
            if i == n:
                return 0

            # Option 1: skip current word
            ans = dfs(i + 1)

            # Option 2: take current word if possible
            ok = True
            for j in range(26):
                if wordCnt[i][j] > cnt[j]:
                    ok = False
                    break

            if ok:
                for j in range(26):
                    cnt[j] -= wordCnt[i][j]

                ans = max(ans, wordScore[i] + dfs(i + 1))

                for j in range(26):
                    cnt[j] += wordCnt[i][j]

            return ans

        return dfs(0)