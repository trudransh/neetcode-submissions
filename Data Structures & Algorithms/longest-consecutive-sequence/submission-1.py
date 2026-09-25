class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for i in numset:
            #check if its a start of a sequence and check that by simply checking if it has a consecutive left number 
            # we use set so that we can do O(1) lookup if we find a nuber with no left neighbour, we will move to check
            # the right neighbourin present in the set, and we continue to do so untill we reach with noo right nos. 
            # and we continue updating out longest number. 

            if (i - 1) not in numset: # here it is important to use numset or else u will get duplicates
                length = 0
                while (i + length) in numset: # i + length is like i is 4 and len i s 0
                    length += 1
                longest = max(length, longest)
        return longest