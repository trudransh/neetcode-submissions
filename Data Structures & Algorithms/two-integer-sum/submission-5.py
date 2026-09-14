class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            A = target - nums[i]
            if A in hmap:
                return [hmap.get(A),i]
            else:
                hmap[nums[i]] = i
            
