from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       m = nums[0]
       n = len(nums)
       c = 0

       for i in range(0,n):
        if nums[i] == m:
            c += 1
        elif c==0:
            m = nums[i]
            c += 1
        else: c -= 1   

       return m 