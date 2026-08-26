from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # 1. Use defaultdict to avoid manual "if key not in dict" checks
        groups = defaultdict(list)
        
        for word in strs:
            # 2. In-line the key generation directly inside the dict access.
            # This avoids creating extra variable references in memory!
            groups["".join(sorted(word))].append(word)
            
        return list(groups.values())