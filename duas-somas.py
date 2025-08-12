# Duas somas

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vistos = {}

        for i, num in enumerate(nums):
            complemento = target - num

            if complemento in vistos:
                return [vistos[complemento], i]
        
            vistos[num] = i

        return vistos # type: ignore


s = Solution()

print(s.twoSum([2,7,11,15], 9))