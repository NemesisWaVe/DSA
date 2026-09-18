class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        l=0
        maxLen=0
        maxFreq=0
        for r in range(len(s)):
            count[s[r]]=count.get(s[r],0)+1
            maxFreq=max(maxFreq,count.get(s[r]))
            while (r-l+1-maxFreq)>k:
                count[s[l]]-=1
                l+=1
            maxLen=max(maxLen,(r-l+1))
        return maxLen
