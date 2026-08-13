class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)

        # node = [left_char, right_char, prefix, suffix, best]
        tree = [None] * (4 * n)

        def combine(left, right, left_len, right_len):
            lc, rc, lp, ls, lb = left
            lc2, rc2, rp, rs, rb = right

            best = max(lb, rb)

            if rc == lc2:
                best = max(best, ls + rp)

            prefix = lp
            if lp == left_len and lc == lc2:
                prefix = left_len + rp

            suffix = rs
            if rs == right_len and rc == rc2:
                suffix = right_len + ls

            return [lc, rc2, prefix, suffix, best]

        def build(node, l, r):
            if l == r:
                tree[node] = [s[l], s[l], 1, 1, 1]
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = combine(
                tree[node * 2],
                tree[node * 2 + 1],
                mid - l + 1,
                r - mid
            )

        def update(node, l, r, index, char):
            if l == r:
                tree[node] = [char, char, 1, 1, 1]
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, r, index, char)

            tree[node] = combine(
                tree[node * 2],
                tree[node * 2 + 1],
                mid - l + 1,
                r - mid
            )

        build(1, 0, n - 1)

        ans = []

        for char, index in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, index, char)
            ans.append(tree[1][4])

        return ans