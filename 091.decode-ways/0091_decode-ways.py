class Solution(object):
    def numDecodings(self, s: str):
        
        if not s:
            return 0

        length = len(s)

        dp = [1 for i in range(length+1)]
        
        if int(s[0]) == 0:
            dp[1] = 0

        for i in range(1, length):
            det1 = 1
            if int(s[i]) == 0:
                det1 = 0
                
            num = int(s[i-1]) * 10 + int(s[i])
            det2 = 0
            if 10 <= num <= 26:
                det2 = 1

            dp[i+1] = det1 * dp[i] + det2 * dp[i-1]

        return dp[-1]

if __name__ == "__main__":
    y = Solution()
    x = '123'
    print(y.numDecodings(x))
