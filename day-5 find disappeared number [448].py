class Solution(object):
    def findDisappearedNumbers(self, nums):
        count=set(nums)
        result=[]
        for i in range(1, len(nums)+1):
            if i not in count:
                result.append(i)
        return result
            
        
