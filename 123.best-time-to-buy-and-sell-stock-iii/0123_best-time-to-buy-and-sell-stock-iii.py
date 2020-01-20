class Solution:
    def maxProfit(self, prices):
        
        if len(prices) < 2:
            return 0

        maxval = prices[1] - prices[0]
        for i in range(2, len(prices)-1):
            print(i, maxval, self.helper(prices[:i]) + self.helper(prices[i:]))
            maxval = max( maxval, self.helper(prices[:i]) + self.helper(prices[i:]) )
            
        return max( maxval, self.helper(prices) )

    # max 1 transaction
    def helper(self, prices):
        ans = 0
        pre = prices[0]
        for i in range(1, len(prices)):
            pre = min(pre, prices[i])
            ans = max(prices[i] - pre, ans)
        return ans

if __name__ == "__main__":
    y = Solution()
    x = [3, 3, 5, 0, 0, 3, 1, 4]
    # x = [1, 2, 3, 4, 5]
    print(x, 'expect = 6, actual = ', y.maxProfit(x))