from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r,maxProfit = 0,1,0

        while r < len(prices):

            if prices[l] < prices[r]:
                maxProfit = max(prices[r]-prices[l] , maxProfit)

            else:
                l =r 
            
            r += 1
        
        return maxProfit

if __name__ == "__main__":
    solution = Solution()
    stockPrices = [13,3,2,3,1,9,4,3,5,2,11]
    maxProfit = solution.maxProfit(stockPrices)
    print(maxProfit)
