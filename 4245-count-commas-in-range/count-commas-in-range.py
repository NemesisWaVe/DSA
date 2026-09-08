class Solution:
    def countCommas(self, n: int) -> int:
        comma=0
        if n>=1000:
            comma+=(min(n,999999)-1000+1)*1
        if n>=1000000:
            comma+=(min(n,999999999)-1000000+1)*2
        if n>=1000000000:
            comma+=(min(n,999999999999)-1)*3
        return comma