class Solution(object):
    def smallestSubsequence(self, s, k, letter, repetition):
        """
        :type s: str
        :type k: int
        :type letter: str
        :type repetition: int
        :rtype: str
        """

        stack = []

        # How many required letters we still need
        required = repetition

        # How many required letters are still available
        remaining_letters = s.count(letter)

        for i, ch in enumerate(s):

            # Remove larger characters when it is safe
            while (
                stack
                and stack[-1] > ch
                and len(stack) + len(s) - i - 1 >= k
                and (stack[-1] != letter or remaining_letters > required)
            ):
                if stack.pop() == letter:
                    required += 1

            # Add current character if possible
            if len(stack) < k:

                if ch == letter:
                    stack.append(ch)
                    required -= 1

                elif k - len(stack) > required:
                    stack.append(ch)

            # Current character is no longer available
            if ch == letter:
                remaining_letters -= 1

        return ''.join(stack)