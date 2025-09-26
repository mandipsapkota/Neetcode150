from typing import List

# BRUTE FORCE APPROACH
class BruteForceSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_set = set()
        for i,num1 in enumerate(nums):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return[i,j]
                
# ONE PASS APPROACH
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,n in enumerate(nums):
            if (target - n) in hashmap:
                return ([hashmap[target - n],i])
            else : 
                hashmap[n] = i


if __name__ == "__main__":
    solution = BruteForceSolution()
    GivenList = [1,3,2,4]
    target = 7
    print(solution.twoSum(GivenList,target))  