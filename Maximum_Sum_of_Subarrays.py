# nums = [2, 1, 5, 1, 3, 2]
# k = 3  , Output: 9

class Solution:
    def maxSum(self, nums: list[int], k: int):
        n =len(nums)
        max_sum=0

        for i in range(n-k + 1):
            current_sum =0
            for j in range(k):
                current_sum += nums[i+j]
                max_sum =max(max_sum, current_sum)
        return max_sum
    
nums = [2, 1, 5, 1, 3, 2]
k = 3   
solution = Solution()
print(solution.maxSum(nums, k))