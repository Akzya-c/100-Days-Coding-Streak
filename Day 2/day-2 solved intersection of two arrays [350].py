class Solution(object):
    def intersect(self, nums1, nums2):
        result=[]
        for num in nums2:
            if num in nums1:
                result.append(num)
                nums1.remove(num)
        return result
sol=Solution()
nums1=[1,2,2,1]
nums2=[2,2]
print(sol.intersect(nums1,nums2))
