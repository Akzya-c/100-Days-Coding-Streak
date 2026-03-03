        result=[]
        for num in nums2:
            if num in nums1:
                result.append(num)
                nums1.remove(num)
        return result

