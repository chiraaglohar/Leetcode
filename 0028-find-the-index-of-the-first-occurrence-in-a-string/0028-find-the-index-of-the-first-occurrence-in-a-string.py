class Solution:
    def strStr(self, haystack, needle):
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i
        return -1