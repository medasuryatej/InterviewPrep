class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for eachElement in nums1:
            position = nums2.index(eachElement)
            elementFound = False
            for newEle in nums2[position:]:
                if newEle > eachElement:
                    output.append(newEle)
                    elementFound = True
                    break
            if not elementFound:
                output.append(-1)
        return output
                