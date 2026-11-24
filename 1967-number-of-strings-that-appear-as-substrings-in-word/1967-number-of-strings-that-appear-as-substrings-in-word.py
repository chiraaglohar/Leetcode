class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return  sum(1 for pat in patterns if pat in word)