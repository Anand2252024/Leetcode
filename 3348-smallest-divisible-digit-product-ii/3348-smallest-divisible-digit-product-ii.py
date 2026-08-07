class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # ---- 1. Factor t into powers of 2,3,5,7 only ----
        primes = [2, 3, 5, 7]
        tt = t
        exp = [0, 0, 0, 0]
        for i, p in enumerate(primes):
            while tt % p == 0:
                tt //= p
                exp[i] += 1
        if tt != 1:
            return "-1"

        E2, E3, E5, E7 = exp
        dims = (E2 + 1, E3 + 1, E5 + 1, E7 + 1)

        digit_contrib = {
            1: (0, 0, 0, 0),
            2: (1, 0, 0, 0),
            3: (0, 1, 0, 0),
            4: (2, 0, 0, 0),
            5: (0, 0, 1, 0),
            6: (1, 1, 0, 0),
            7: (0, 0, 0, 1),
            8: (3, 0, 0, 0),
            9: (0, 2, 0, 0),
        }

        def idx_of(s):
            i2, i3, i5, i7 = s
            return ((i2 * dims[1] + i3) * dims[2] + i5) * dims[3] + i7

        # ---- 2. dp[state] = min number of digits needed to satisfy 'state' ----
        size = dims[0] * dims[1] * dims[2] * dims[3]
        states = []
        for i2 in range(dims[0]):
            for i3 in range(dims[1]):
                for i5 in range(dims[2]):
                    for i7 in range(dims[3]):
                        states.append((i2, i3, i5, i7))
        states.sort(key=sum)

        dp = [0] * size
        for s in states:
            if sum(s) == 0:
                dp[idx_of(s)] = 0
                continue
            best = float('inf')
            for d in range(2, 10):
                c = digit_contrib[d]
                ns = (max(s[0] - c[0], 0), max(s[1] - c[1], 0),
                      max(s[2] - c[2], 0), max(s[3] - c[3], 0))
                if ns == s:
                    continue
                val = dp[idx_of(ns)] + 1
                if val < best:
                    best = val
            dp[idx_of(s)] = best

        def need(state):
            return dp[idx_of(state)]

        n = len(num)
        digits = [int(ch) for ch in num]
        target = (E2, E3, E5, E7)

        # ---- 3. prefix info: zero flag + cumulative exponents ----
        prefix_zero = [False] * (n + 1)
        prefE = [(0, 0, 0, 0)] * (n + 1)
        for i in range(n):
            prefix_zero[i + 1] = prefix_zero[i] or (digits[i] == 0)
            c = digit_contrib.get(digits[i], (0, 0, 0, 0))
            pe = prefE[i]
            prefE[i + 1] = (pe[0] + c[0], pe[1] + c[1], pe[2] + c[2], pe[3] + c[3])

        # ---- 4. check num itself ----
        if not prefix_zero[n]:
            total = prefE[n]
            if all(total[k] >= target[k] for k in range(4)):
                return num

        # ---- 5. try to fix a suffix, keeping the longest possible prefix ----
        found_i = -1
        found_digit = -1
        found_req = None
        for i in range(n - 1, -1, -1):
            if prefix_zero[i]:
                continue
            req = tuple(max(target[k] - prefE[i][k], 0) for k in range(4))
            remaining_after = n - 1 - i
            for d in range(digits[i] + 1, 10):
                c = digit_contrib[d]
                new_req = tuple(max(req[k] - c[k], 0) for k in range(4))
                if remaining_after >= need(new_req):
                    found_i, found_digit, found_req = i, d, req
                    break
            if found_i != -1:
                break

        if found_i != -1:
            result = digits[:found_i] + [found_digit]
            c = digit_contrib[found_digit]
            state = tuple(max(found_req[k] - c[k], 0) for k in range(4))
            remaining_positions = n - 1 - found_i
            for pos in range(remaining_positions):
                rem_after = remaining_positions - pos - 1
                for d in range(1, 10):
                    cc = digit_contrib[d]
                    ns = tuple(max(state[k] - cc[k], 0) for k in range(4))
                    if rem_after >= need(ns):
                        result.append(d)
                        state = ns
                        break
            return ''.join(map(str, result))

        # ---- 6. no same-length fix works -> need a longer number ----
        L = max(n + 1, need(target))
        result = []
        state = target
        for pos in range(L):
            rem_after = L - pos - 1
            for d in range(1, 10):
                cc = digit_contrib[d]
                ns = tuple(max(state[k] - cc[k], 0) for k in range(4))
                if rem_after >= need(ns):
                    result.append(d)
                    state = ns
                    break
        return ''.join(map(str, result))