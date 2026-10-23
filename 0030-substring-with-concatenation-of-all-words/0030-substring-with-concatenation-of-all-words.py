from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []
        n, m, length = len(s), len(words), len(words[0])
        if m * length > n:
            return ans
        need = Counter(words)

        for offset in range(length):
            seen = {}
            left, count = offset, 0
            for right in range(offset, n - length + 1, length):
                word = s[right:right + length]
                if word not in need:
                    seen = {}
                    left, count = right + length, 0
                    continue
                seen[word] = seen.get(word, 0) + 1
                count += 1
                while seen[word] > need[word]:
                    old = s[left:left + length]
                    seen[old] -= 1
                    left += length
                    count -= 1
                if count == m:
                    ans.append(left)
                    old = s[left:left + length]
                    seen[old] -= 1
                    left += length
                    count -= 1
        return ans