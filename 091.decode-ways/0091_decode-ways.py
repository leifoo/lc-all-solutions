class Solution(object):
    def numDecodings(self, s: str):
        
        if not s:
            return 0

        length = len(s)

        dp = [1 for i in range(length + 1)]

        for i in range(1, length):
            num = int(s[i-1]) * 10 + int(s[i])
            det = 0
            if 0 < num < 27:
                det = 1

            dp[i+1] = dp[i] + det * dp[i-1]

        return dp[-1]

if __name__ == "__main__":
    y = Solution()
    x = '123'
    print(y.numDecodings(x))