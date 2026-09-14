from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map=defaultdict(list)
        for word in strs:
            signature=tuple(sorted(word))
            anagram_map[signature].append(word)
        return list(anagram_map.values())
