class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        n = len(s)

        # Segment tree node:
        # left character, right character,
        # longest prefix, longest suffix, longest answer
        # and length
        tree = [None] * (4 * n)

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            length = a[5] + b[5]

            left_char = a[0]
            right_char = b[1]

            prefix = a[2]
            if a[2] == a[5] and a[1] == b[0]:
                prefix = a[5] + b[2]

            suffix = b[3]
            if b[3] == b[5] and a[1] == b[0]:
                suffix = b[5] + a[3]

            best = max(a[4], b[4])

            if a[1] == b[0]:
                best = max(best, a[3] + b[2])

            return (
                left_char,
                right_char,
                prefix,
                suffix,
                best,
                length
            )

        def build(node, l, r):
            if l == r:
                tree[node] = (s[l], s[l], 1, 1, 1, 1)
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, idx, ch):
            if l == r:
                tree[node] = (ch, ch, 1, 1, 1, 1)
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, r, idx, ch)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        build(1, 0, n - 1)

        answer = []

        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            answer.append(tree[1][4])

        return answer