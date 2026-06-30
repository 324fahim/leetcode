class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        seenDigit = False
        seenDot = False
        seenExp = False

        for i, c in enumerate(s):
            if c.isdigit():
                seenDigit = True

            elif c in "+-":
                if i > 0 and s[i - 1] not in "eE":
                    return False

            elif c == ".":
                if seenDot or seenExp:
                    return False
                seenDot = True

            elif c in "eE":
                if seenExp or not seenDigit:
                    return False
                seenExp = True
                seenDigit = False

            else:
                return False

        return seenDigit