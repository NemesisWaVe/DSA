class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2=len(s1),len(s2)
        if n1>n2:
            return False
        s1Ctr={}
        windowCtr={}
        for i in range(n1):
            s1Ctr[s1[i]]=s1Ctr.get(s1[i],0)+1
            windowCtr[s2[i]]=windowCtr.get(s2[i],0)+1
        if s1Ctr==windowCtr:
            return True
        l=0
        for r in range(n1,n2):
            incoming=s2[r]
            windowCtr[incoming]=windowCtr.get(incoming,0)+1
            outgoing=s2[l]
            windowCtr[outgoing]-=1
            if windowCtr[outgoing]==0:
                del windowCtr[outgoing]
            l+=1
            if s1Ctr==windowCtr:
                return True
        return False
