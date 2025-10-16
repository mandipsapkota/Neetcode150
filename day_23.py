from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+" , "-" , "/" , "*"]

        for token in tokens:

            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                a,b = stack.pop() , stack.pop()
                stack.append(b-a)

            elif token == "*":
                stack.append(stack.pop() * stack.pop())

            elif token == "/":
                a,b = stack.pop() , stack.pop()
                stack.append(int(b/a))

            else:
                stack.append(int(token))

        return stack[-1]

if __name__ == "__main__":
    solution = Solution()
    demoList = ["1","2","+","3","*","9","+"]
    print("Accepted") if solution.evalRPN(demoList) == 18 else print("Rejected")