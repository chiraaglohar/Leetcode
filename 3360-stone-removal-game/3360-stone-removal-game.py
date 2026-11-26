class Solution:
    def canAliceWin(self, n: int) -> bool:
        missing = 55 - n 
        unplayed = round(sqrt(2 * missing))  
        return unplayed % 2 == 1  