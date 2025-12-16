from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        min_val = min(nums)
        max_val = max(nums)

        freq = [0] * (max_val - min_val + 1)
        res = []

        # Count frequency using shifted index
        for n in nums:
            freq[n - min_val] += 1 # -ve no. handling

        # Collect unique numbers (shift back to original values)
        for i in range(len(freq)):
            if freq[i] >= 1:
                res.append(i + min_val)

        # Copy unique elements back to nums
        for i in range(len(res)):
            nums[i] = res[i]

        return len(res)
