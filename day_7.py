from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result , i= [1]*len(nums) , 0

        # prefix
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= postfix
            postfix *= nums[i]


        return result

if __name__ == "__main__":
    nums = [1,2,3,4]
    solution = Solution()
    result = solution.productExceptSelf(nums=nums)
    print(result)
