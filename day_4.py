from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # res = {character count : list of anagrams}
        res = defaultdict(list)  # Use lowercase 'list' instead of 'List'

        for s in strs:
            count = [0]*26  # a to z

            for c in s:
                count[ord(c) - ord("a")] += 1
                  
            res[tuple(count)].append(s)

        return list(res.values())
    
if __name__ == "__main__":
    solution = Solution()
    list1 = ["list","slit","tea","pea","eat"]
    print(solution.groupAnagrams(list1))  
