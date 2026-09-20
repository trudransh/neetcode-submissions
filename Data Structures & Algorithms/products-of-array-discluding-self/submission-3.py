class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_count = 1, 0
        for i in nums:
            if i == 0 :
                zero_count += 1
            else:
                prod *= i
        if zero_count > 1 : return [0] * len(nums)
        
        res = [0] * len(nums)
        for i,c in enumerate(nums):
            if zero_count == 1:
                if c != 0:
                    res[i] = 0
                else:
                    res[i] = prod
            else: res[i] = prod // c
        return res
        # product solution