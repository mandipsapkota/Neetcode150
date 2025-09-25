# Contains duplicate problem
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums: 
            if n in hashset:
                return True
            hashset.add(n)
        return False


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 4, 1] 
    print(s.hasDuplicate(nums))  
