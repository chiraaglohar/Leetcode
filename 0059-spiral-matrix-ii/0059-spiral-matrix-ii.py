class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        res = [[1]*n for _ in range(n)]
        val = 1
        left,top,right,bottom = 0,0,n-1,n-1
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                res[top][i] = val
                val+=1
            top+=1
            for i in range(top,bottom+1):
                res[i][right] = val
                val+=1
            right-=1
            for i in range(right,left-1,-1):
                res[bottom][i] = val
                val+=1
            bottom-=1
            for i in range(bottom,top-1,-1):
                res[i][left] = val
                val+=1
            left+=1
        return res