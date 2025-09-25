# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# -----------------------------------APPROACH 1 ---------------------------------------------------------

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {},{}

        for i in range(len(s)):
            countS[s[i]] = 1+countS.get(s[i],0)
            countT[t[i]] = 1+countT.get(t[i],0)

        for c in countS:
            if countS[c] != countT.get(c,0):
                return False

        return True


# ----------------------- APPROACH 2 , LESS SPACE COMPLEXITY, but less efficient too. Takes time---------
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
    


if __name__ == "__main__":
    solution = Solution()
    word1 = "luff"
    word2 = "full"
    print(solution.isAnagram(word1,word2))  