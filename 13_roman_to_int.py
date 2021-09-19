class Solution:
    def romanToInt(self, s: str) -> int:
        roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900} 
        roman_str=0
        for i in range(len(s)):            
            if i == 0:
                roman_str+=roman.get(s[i])
            else:
                if s[i-1]=='I':
                    if s[i]=='I':
                        roman_str+=roman.get(s[i])
                    else:
                        roman_str-=1
                        roman_str+=roman.get('I'+s[i])
                
                elif s[i-1]=='X':
                    if s[i]=='X' or s[i]=='V' or s[i]=='I':
                        roman_str+=roman.get(s[i])
                    else:
                        roman_str-=10
                        roman_str+=roman.get('X'+s[i])

                elif s[i-1]=='C':
                    if s[i]=='C' or s[i]=='L' or s[i]=='X' or s[i]=='V' or s[i]=='I':
                        roman_str+=roman.get(s[i])
                    else:
                        roman_str-=100
                        roman_str+=roman.get('C'+s[i])
                else:
                    roman_str+=roman.get(s[i])

        return roman_str
s=Solution()
print(s.romanToInt("MCMXCVI"))