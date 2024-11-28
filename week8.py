# week8.py
# Author: Tianyi Xu
class Solution:
    # 416. Partition Equal Subset Sum
    # Very hard (>﹏<) 
    def canPartition(self, nums):
        if sum(nums) % 2 != 0:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        for i in range(len(nums) - 1):
            nextDP = dp.copy()
            for t in dp:
                nextDP.add(t+nums[i])
            dp = nextDP
        return True if target in dp else False

    # 322. Coin Change
    # Also quite hard :(
    def coinChange(self, coins, amount: int):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(len(dp)):
            for coin in coins:
                if a >= coin:
                    dp[a] = min(dp[a], 1 + dp[a - coin])

        return dp[amount] if dp[amount] != amount + 1 else -1

    # 53. Maximum Subarray
    # Incredibly easy, don't know what it has to do with DP tho
    def maxSubArray(self, nums) -> int:
        theMax = max(nums)
        if theMax < 0:
            return theMax
        currSum = 0
        result = 0
        for i in range(len(nums)):
            currSum += nums[i]
            result = max(currSum, result)
            if (currSum < 0):
                currSum = 0
        return result