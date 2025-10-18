from typing import List 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = [] # temp,index pair is one element on stack
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t,i))

        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.dailyTemperatures([21,23,23,21,34,43,23,25]))