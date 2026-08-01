from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        freqbucket=[[] for _ in range(len(nums)+1)]
        for num,freq in count.items():
            freqbucket[freq].append(num)
        res=[]
        for i in range(len(freqbucket)-1,0,-1):
            for num in freqbucket[i]:
                res.append(num)
                if len(res)==k:
                    return res
