class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        children = [[] for _ in s]
        for x in range(1, len(s)):
            children[parent[x]].append(x)
        size, last = [1] * len(s), {}  
        def dfs(x: int) -> None:
            c = s[x]
            above = last.get(c, -1) 
            last[c] = x
            for child in children[x]:
                dfs(child)
            last[c] = above
            if x:
                size[above if above >= 0 else parent[x]] += size[x]
        dfs(0)
        return size