class Solution(object):
    def maximumGood(self, statements):
        """
        :type statements: List[List[int]]
        :rtype: int
        """
        n = len(statements)
        ans = 0

        for mask in range(1 << n):
            valid = True

            for i in range(n):
                if ((mask >> i) & 1) == 0:
                    continue

                for j in range(n):
                    if statements[i][j] == 2:
                        continue

                    if statements[i][j] == 1:
                        if ((mask >> j) & 1) == 0:
                            valid = False
                            break
                    else:  # statements[i][j] == 0
                        if ((mask >> j) & 1) == 1:
                            valid = False
                            break

                if not valid:
                    break

            if valid:
                ans = max(ans, bin(mask).count("1"))

        return ans