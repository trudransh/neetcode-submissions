class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ana = defaultdict(list)
        for s in strs:
            sorted_string = ''.join(sorted(s))
            ana[sorted_string].append(s)
        return list(ana.values())