class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}  

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  
print(sol.twoSum([3, 2, 4], 6))       
print(sol.twoSum([3, 3], 6))          
