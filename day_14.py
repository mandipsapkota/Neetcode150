from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

        if not height : return 0

        l,r, area = 0,len(height) - 1,0
        leftMax,rightMax = height[l],height[r]

        while l<r:
            if leftMax < rightMax :
                l+=1
                leftMax = max(leftMax,height[l])
                area += leftMax - height[l]
            else:
                r-=1
                rightMax = max(rightMax,height[r])
                area += rightMax - height[r]
        return area


if __name__ == "__main__":
    solution = Solution()
    list = [1,3,2,4,5,2,3,3]
    result = solution.trap(list)
    print(result)