class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mapy = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            mapy[sortedS].append(s)
        return list(mapy.values())