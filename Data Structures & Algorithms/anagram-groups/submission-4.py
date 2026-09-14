class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            f_array = [0]*26
            for c in s:
                f_array[ord(c) - ord('a')] += 1
            res[tuple(f_array)].append(s)
        return list(res.values())