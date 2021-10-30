class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s='Hello World'

        return len(s[::-1].lstrip().split(sep=' ', maxsplit=1)[0])

x=Solution()
print(x.lengthOfLastWord('Hello World'))
