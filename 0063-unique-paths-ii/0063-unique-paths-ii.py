class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[0][0] == 1: return 0 
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[1][1] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                if obstacleGrid[i][j] == 0:
                    dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j]
        return dp[m][n]