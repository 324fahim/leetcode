class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        # Count characters
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # Build counts for the left half
        half = [x // 2 for x in freq]

        # Middle character (only one can have odd frequency)
        middle = ""
        for i in range(26):
            if freq[i] % 2 == 1:
                middle = chr(i + ord('a'))
                break

        n = len(s) // 2

        # Calculate number of distinct permutations,
        # but stop once we reach k.
        def count_permutations(cnt, total):
            ways = 1

            for i in range(26):
                c = cnt[i]

                for j in range(1, c + 1):
                    ways = ways * (total - c + j) // j

                    if ways >= k:
                        return k

                total -= c

            return ways

        total_ways = count_permutations(half, n)

        if total_ways < k:
            return ""

        # Construct the k-th lexicographically smallest left half
        left = []

        for pos in range(n):
            for c in range(26):

                if half[c] == 0:
                    continue

                # Temporarily place character c
                half[c] -= 1

                remaining = n - pos - 1

                ways = count_permutations(half, remaining)

                if k > ways:
                    # Not enough permutations here.
                    # Skip this block.
                    k -= ways
                    half[c] += 1
                else:
                    # This is the correct character.
                    left.append(chr(c + ord('a')))
                    break

        left = ''.join(left)

        return left + middle + left[::-1]