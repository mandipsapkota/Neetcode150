from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        res = r

        while l<=r:
            k = (l+r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)

            if hours <= h:
                res = min(res,k)
                r = k-1
            
            else:
                l = k+1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.minEatingSpeed([2,3,4,4,5,6,7],5))
