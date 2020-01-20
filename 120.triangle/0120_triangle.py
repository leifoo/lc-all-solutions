class Solution:
    def minimumTotal(self, triangle):
        
        if not triangle or not triangle[0]:
            return []

        length = len(triangle)
        size = 2 ** (len(triangle) - 1)
        minval = sum( [triangle[i][0] for i in range(length)] )

        for i in range(size):
            temp = triangle[0][0]
            index = 0
            for j in range(1, length):
                num = 2 ** (length - j)
                index += i // num
                i = i % num
                print(i,j, index)
                temp += triangle[j][index]
            minval = min( minval, temp )

        return minval


if __name__ == "__main__":
    y = Solution()
    x = [
        [2],
        [3,4],
        [6,5,7],
        [4,1,8,3]
        ]

    print(x, y.minimumTotal(x))


