class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        n = len(num)

        def dfs(pos, path, value, last):
            if pos == n:
                if value == target:
                    res.append(path)
                return

            for i in range(pos, n):
                # Prevent numbers with leading zeros
                if i > pos and num[pos] == '0':
                    break

                cur_str = num[pos:i + 1]
                cur = int(cur_str)

                if pos == 0:
                    dfs(i + 1, cur_str, cur, cur)
                else:
                    # Addition
                    dfs(i + 1, path + "+" + cur_str, value + cur, cur)

                    # Subtraction
                    dfs(i + 1, path + "-" + cur_str, value - cur, -cur)

                    # Multiplication
                    dfs(i + 1,
                        path + "*" + cur_str,
                        value - last + last * cur,
                        last * cur)

        dfs(0, "", 0, 0)
        return res