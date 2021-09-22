class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=='' :
            return '0'
        elif needle in haystack and len(haystack)>0:
            haystack1=haystack.replace(str(needle[::]),'0')
            return haystack1.index('0')
        else:
            return '-1'
s=Solution()
print(s.strStr("Hello","ll"))


    
    
