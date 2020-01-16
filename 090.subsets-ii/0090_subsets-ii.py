class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(index = 0, path = []):
            if path not in ans:
                ans.append(path)
            [dfs(i + 1, path + [nums[i]]) for i in range(index, len(nums))]

        ans = []
        nums = sorted(nums)
        dfs()
        return ans

if __name__ == "__main__": 
    y = Solution()
    x = [1, 2, 2]
    print("subsets(", x, ') = ', y.subsets(x))
