class Solution():
    def grayCode(self, n: int):

        if n < 1:
            return []

        ans = [0]
        for i in range(n):
            tmp = 2 ** i
            ans.extend([x + tmp for x in ans[::-1]])

        return ans


if __name__ == "__main__":
    y = Solution()
    n = 4
    print(y.grayCode(n))

