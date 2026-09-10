class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = set()
        if not nums:
            return False
        for i in nums:
            if i not in count:
                count.add(i)
            else:
                return True
        return False