from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        @lru_cache(None)
        def match(i: int, j: int) -> bool:
            if j == n:
                return i == m
            first = i < m and (s[i] == p[j] or p[j] == '.')
            if j + 1 < n and p[j + 1] == '*':
                return match(i, j + 2) or (first and match(i + 1, j))
            return first and match(i + 1, j + 1)

        return match(0, 0)