class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and suffix approach ( not optimal )
        n = len(nums)
        p,s,res = [0] * n,[0] * n,[0] * n
        p[0] = s[n - 1] = 1
        # calculating prefix array
        for i in range(1,n):
            p[i] = nums[i - 1] * p[i - 1]
        for i in range(n-2, -1, -1): # here the i can never be -1, it will stop before 
            s[i] = nums[i+1] * s[i+1]
        for i in range(n):
            res[i] = s[i] * p[i]
        return res