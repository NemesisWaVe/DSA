class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            while l<r and not self.alphaNum(s[l]):
                l+=1
            while l<r and not self.alphaNum(s[r]):
                r-=1
            if s[l].lower()==s[r].lower():
                l+=1
                r-=1
            else:
                return False
        return True
    def alphaNum(self,c):
        val=ord(c)
        return (ord('A')<=val<=ord('Z') or
               ord('a')<=val<=ord('z') or
               ord ('0')<=val<=ord('9'))

            