class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return False
        window={}
        ctr={}
        for char in t:
            ctr[char]=ctr.get(char,0)+1
        have=0
        need=len(ctr)
        res=[float("inf"),-1,-1]
        l=0
        for r in range(len(s)):
            char=s[r]
            window[char]=window.get(char,0)+1
            if char in ctr and window[char]==ctr[char]:
                have+=1
            while have==need:
                window_len=r-l+1
                if window_len<res[0]:
                    res=[window_len,l,r]
                left_char=s[l]
                window[left_char]-=1
                if left_char in ctr and window[left_char]<ctr[left_char]:
                    have-=1
                l+=1
        lidx,ridx=res[1],res[2]
        return s[lidx:ridx+1] if res[0]!=float("inf") else ""
