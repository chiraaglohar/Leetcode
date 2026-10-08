class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        count = 0

        for c in s:
            if c == '(':
                if count > 0:
                    ans.append(c)
                count += 1
            else:
                count -= 1
                if count > 0:
                    ans.append(c)

        return "".join(ans)