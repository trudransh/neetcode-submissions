class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            sortedS = "".join(sorted(s))
            anagrams[sortedS].append(s)
        return list(anagrams.values())