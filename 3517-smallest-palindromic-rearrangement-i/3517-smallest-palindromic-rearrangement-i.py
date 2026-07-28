class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = [0] * 26

        # Count characters
        for c in s:
            count[ord(c) - ord('a')] += 1

        left = []
        middle = ""

        # Build the smallest possible left half
        for i in range(26):
            if count[i] % 2 == 1:
                middle = chr(i + ord('a'))

            left.append(chr(i + ord('a')) * (count[i] // 2))

        left = ''.join(left)

        # Mirror the left half
        return left + middle + left[::-1]