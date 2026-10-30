class Solution:
    def RLE(self, sequence):
        curr = sequence[0]
        count = 0
        ans = ""
        
        
        for num in sequence:
            if curr == num:
                count += 1
            else:
                ans += f'{count}{curr}'
                curr = num
                count = 1
        
        
        return ans + f'{count}{curr}'
    
    
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        
        return self.RLE(self.countAndSay(n - 1))