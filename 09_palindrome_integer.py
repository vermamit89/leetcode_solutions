class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        x_str=str(x)
        x_str_rev=x_str[::-1]
        if x_str==x_str_rev:
            return True
        else:
            return False
       
s=Solution()
print(s.isPalindrome(1000021))
