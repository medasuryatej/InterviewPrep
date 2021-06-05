def merge(nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        print(nums1)
        if n > 0:
            nums1[:n] = nums2[:n]


nums1 = [1,5,8,0,0,0,0,0,0,0,0,0]
m = 3
nums2 = [2,3,6,7,8,9,10,11,13] 
n = 9
merge(nums1, m, nums2, n)
print(nums1)