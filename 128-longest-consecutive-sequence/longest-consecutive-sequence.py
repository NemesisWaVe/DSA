class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCtr=0
        numset=set(nums)
        for num in numset:
            ctr=0
            if num-1 not in numset:
                while num in numset:
                    num+=1
                    ctr+=1
            maxCtr=max(ctr,maxCtr)
        return maxCtr