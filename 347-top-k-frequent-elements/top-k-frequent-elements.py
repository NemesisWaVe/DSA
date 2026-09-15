from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt=Counter(nums)
        ordered=sorted(cnt.items(),key=lambda pair:pair[1],reverse=True)
        return [num for num,count in ordered[:k]]