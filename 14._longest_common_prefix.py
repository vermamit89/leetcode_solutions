class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if strs==[""]:
            return ""
        
        elif strs!=0 and len(strs) == 1:
            return strs[0]
        else:
            strs.sort()
            lcp = ""
            for i in range(len(strs[0])):
                if strs[0][i] == strs[-1][i]:
                    lcp += strs[0][i]
                elif strs[0][0] !=strs[-1][0]:
                    return ""
                    break
                else:
                    break
            return lcp
    
s=Solution()
print(s.longestCommonPrefix(["ab","abc","abcd"]))