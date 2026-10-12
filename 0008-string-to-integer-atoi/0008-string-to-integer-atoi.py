class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        i = 0
        sign = 1
        max_int = 2**31 - 1
        min_int = -2**31
        
        if len(s) == 0:
            return 0
        
        # Remove leading whitespaces
        while i < len(s) and s[i] == ' ':
            i += 1
        
        # Check for sign
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        # Convert digits to integer
        while i < len(s) and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            if ans > max_int // 10 or (ans == max_int // 10 and digit > max_int % 10):
                return max_int if sign == 1 else min_int
            ans = ans * 10 + digit
            i += 1
        
        return ans * sign