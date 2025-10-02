from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                longest = max(length, longest)

        return longest
    
if __name__ == "__main__":
    myList = [1,2,3,5,6,8,4,66,77]
    solution = Solution()
    longest = solution.longestConsecutive(nums = myList)
    print(longest)