from typing import List
import collections

# BRUTE FORCE 
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
    
# DEQUE
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()
        l = r = 0
        while r<len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            # remove left val from window 
            if l>q[0]:
                q.popleft()

            if (r+1)>=k:
                res.append(nums[q[0]])
                l+= 1

            r += 1
        return res
    
# INFERENCE

if __name__ == "__main__":
    solution = Solution()
    nums= [2,5,3,5,3,6,3,5,3,6,4]
    k = 3
    print(solution.maxSlidingWindow(nums,k))