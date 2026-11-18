class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[0][0] == 1: return 0 # if the first cell is itself an obstacle

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0]*(n+1) for _ in range(m+1)] # first row and first column are false

        dp[1][1] = 1 # starting point (one possible way)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue # skip the very first cell (starting point)

                if obstacleGrid[i][j] == 0:
                    dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] # compute only when it is not an obstacle
        
        return dp[m][n]