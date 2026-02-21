class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        s1CTR = {}
        windowctr = {}
        
        # 1. Setup FIRST window (Only loop up to the length of s1)
        for i in range(len(s1)):
            s1CTR[s1[i]] = 1 + s1CTR.get(s1[i], 0)
            windowctr[s2[i]] = 1 + windowctr.get(s2[i], 0)
            
        if s1CTR == windowctr:
            return True
            
        l = 0
        # 2. Slide the window across the rest of s2
        for r in range(len(s1), len(s2)):
            # Step A: Add new character entering from the right
            windowctr[s2[r]] = 1 + windowctr.get(s2[r], 0)
            
            # Step B: Remove old character leaving from the left
            windowctr[s2[l]] -= 1
            
            # THE GHOST ZERO FIX: If count hits 0, delete the key entirely!
            if windowctr[s2[l]] == 0:
                del windowctr[s2[l]] # or windowctr.pop(s2[l])
                
            l += 1
            
            # Compare the clean dictionaries
            if s1CTR == windowctr:
                return True
                
        return False