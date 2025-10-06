from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l,r,result = 0,len(heights) - 1,0

        while l<r:
            new = min(heights[l],heights[r]) * (r-l)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

            if new > result:
                result = new

        return result

if __name__ == "__main__":
    solution = Solution()
    myList = [1,2,5,3,6,7,8,2]
    result = solution.maxArea(heights=myList)
    print(result)
