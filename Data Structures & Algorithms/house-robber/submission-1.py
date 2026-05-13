class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):

            # no houses left
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]
            # option 1: skip current house
            skip = dfs(i +1)

            #option 2: rob current house
            rob = nums[i] + dfs(i + 2)

            #choose the best option
            memo[i] = max(skip, rob)
            return memo[i]
            
        return dfs(0)
        