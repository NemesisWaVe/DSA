class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCTR=0
        numset=set(nums)
        for curr in numset:
            if curr-1 not in numset:
                ctr=1
                while (curr+1) in numset:
                    ctr+=1
                    curr+=1
                maxCTR=max(ctr,maxCTR)
        return maxCTR