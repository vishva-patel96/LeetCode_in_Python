class Solution:
    def threeSum(self, nums: list[int]):
            if(len(nums)<3):
                return []
            elif(len(nums)==3 and sum(nums)==0):
                return [nums]
            nums = sorted(nums)

            i = 0
            Solution  = []
            while i < len(nums)-2:
                if i> 0 and nums[i]==nums[i-1]:
                    i += 1
                    continue
                j = i + 1
                k = len(nums)- 1
                target = 0 - nums[i]
                while (j < k ):
                     if j > i+1 and nums[j]==nums[j-1]:
                        j += 1
                        continue
                     if k < len(nums) -1 and nums[k]==nums[k+1]:
                        k -= 1
                        continue
                     jksum = nums[j] + nums[k]
                     if jksum == target:
                        Solution.append([nums[i], nums[j], nums[k]])
                    
                     if jksum > target:
                        k -=1
                     else: 
                        j +=1
                i += 1
                     
            return Solution
nums = [-1,0,1,2,-1,-4]
solution = Solution()
print(solution.threeSum(nums))