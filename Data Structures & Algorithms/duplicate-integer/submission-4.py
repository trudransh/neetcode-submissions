class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = set()
        if not nums:
            return False
        for i in nums:
            if i in count:
                return True
            count.add(i)            
        return False