from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characterSet = set()
        l,r = 0,1
        res = 0

        for r in range(len(s)):
            while s[r] in characterSet:
                characterSet.remove(s[l])
                l+=1
            characterSet.add(s[r])
            res = max(res,r-l+1)
        return res


if __name__ == "__main__":
    solution = Solution()
    s = "iammandip"
    res = solution.lengthOfLongestSubstring(s)
    print(res)
