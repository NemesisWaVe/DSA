class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2=len(s1),len(s2)
        if n1>n2:
            return False
        s1ctr={}
        windowctr={}
        for i in range(n1):
            s1ctr[s1[i]]=s1ctr.get(s1[i],0)+1
            windowctr[s2[i]]=windowctr.get(s2[i],0)+1
        if s1ctr==windowctr:
            return True
        l=0
        for r in range(n1,n2):
            incoming=s2[r]
            windowctr[incoming]=windowctr.get(incoming,0)+1
            outgoing=s2[l]
            windowctr[outgoing]-=1
            if windowctr[outgoing]==0:
                del windowctr[outgoing]
            if s1ctr==windowctr:
                return True
            l+=1
        return False