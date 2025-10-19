from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position,speed)]
        stack = []
        for p,s in sorted(pair)[::-1]: #reverse sorted ds
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1]<= stack[-2]:
                stack.pop()
        return len(stack)


if __name__ == "__main__":
    target = 10
    position = [1,4]
    speed = [3,2]
    solution = Solution()
    print(solution.carFleet(target,position,speed))