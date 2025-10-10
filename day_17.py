class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap, res = {},0
        l = 0

        for r in range(len(s)):
            charMap[s[r]] = 1 + charMap.get(s[r],0)

            if (r-l+1) - max(charMap.values()) > k:
                charMap[s[l]] -= 1
                l+=1

            res = max(res,r-l+1)
        return res

if __name__ == "__main__":
    solution = Solution()
    s = "AMMAMAMAMAMAHO"
    k = 2
    print(solution.characterReplacement(s,k))