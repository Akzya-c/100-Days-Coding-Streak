class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False 


sol = Solution()
nums = [1, 2, 3, 1]


print(sol.containsDuplicate(nums))
