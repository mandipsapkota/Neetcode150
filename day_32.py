from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while l<=r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            
            if nums[m] >= nums[l]:
                if target > nums[m] or target<nums[l]:
                    l = m+1
                else:
                    r = m-1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m-1
                else:
                    l = m+1

        return -1
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.search([4,5,6,7,0,1,2], 0))  # Output: 4
    print(sol.search([4,5,6,7,0,1,2], 3))  # Output: -1
    print(sol.search([1], 0))                # Output: -1
