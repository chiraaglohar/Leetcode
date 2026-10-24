class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n=len(s)
        p = "".join(c for i, c in enumerate(p) if c != "*" or i == 0 or p[i-1] != "*")
        m=len(p)
        @cache
        def dp(i,j):
            if i>=n and j>=m:
                return True
            if j>=m:
                return False
            if i>=n:
                while j<m and p[j]=="*":
                    j+=1
                if j==m:
                    return True
                return False
            if s[i]==p[j] or p[j]=="?":
                return (dp(i+1,j+1))
            elif p[j]=="*":
                return dp(i+1,j) or dp(i,j+1)
            return False
        return dp(0,0)