from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return -1

if __name__ == "__main__":
    solution = Solution()
    nums = [-2,-1,2,3,5,7,9,10]
    target = 9
    print(solution.search(nums,target))