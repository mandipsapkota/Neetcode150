# BRUTE FORCE 
from typing import List
class BruteForceSolution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l,r = 0,k
        maxList = []
        while r<=len(nums):
            element = sorted(nums[l:r])[-1]
            maxList.append(element)
            l+=1
            r+=1
        
        return maxList