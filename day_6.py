from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))+"@"+ s

        return res

    def decode(self, s: str) -> List[str]:
        strs,i = [],0
        while i<len(s):
            j=i
            while s[j] != "@": 
                j += 1

            length = int(s[i:j])
            single_str = s[j+1:j+1+length]
            strs.append(single_str)
            i = j+1+length

        return strs
    
if __name__ == "__main__":
    solution = Solution()
    list1 = ["Programming","Is","Freaking","Awesome"]
    encoded = solution.encode(list1)
    print(encoded)  
    print(solution.decode(encoded))