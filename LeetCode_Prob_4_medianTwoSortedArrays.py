class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
            Given the total number of elements (Array1+Array2)
            the median is the middle element
            so partiton the array1 and array2 such that
            array1 left partition is <= array2 right partition and
            array2 left partition is <= array1 right partition
            if not adjust the partition positions
        """
        # total length
        total = len(nums1) + len(nums2)
        # swapping the order
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        # finding half way mark
        half = total // 2
        # initialize left and right partitions
        left, right = 0, len(nums1) - 1
        while True:
            # nums1 partition
            lmid = left + (right - left) // 2
            # nums2 partition
            rmid = half - lmid - 2 # one subtraaction for nums2 and one for nums1
            # finding boundaries of partitions
            Aleft = nums1[lmid] if lmid >= 0 else float("-inf") # reaching zeroth index of nums1 for partition
            Aright = nums1[lmid+1] if (lmid+1) < len(nums1) else float("inf") # reaching end of nums1 for partition
            Bleft = nums2[rmid] if rmid >= 0 else float("-inf") # reaching zeroth index of nums2 for partition
            Bright = nums2[rmid+1] if (rmid+1) < len(nums2) else float("inf")
            
            # check if partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2 != 0:
                    return min(Bright, Aright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # Aleft is too much (too many elements in nums1 is considered)
            elif Aleft > Bright:
                right = lmid - 1
            # Bleft is too much
            else:
                left = lmid + 1
         