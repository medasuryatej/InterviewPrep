class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        lra = max(heights)
        
        for index, height in enumerate(heights):
            # print(stack, lra)
            if not stack:
                stack.append((index, height))
                continue
            start = index
            
            # stack top is greater than current element height
            # so cannot propogate the previous height further
            while stack and stack[-1][1] > height:
                # pop the stack top
                topI, topH = stack.pop()
                # see if the stack top can contribute to max area
                lra = max(lra, topH * (index - topI))
                # since the stack top is larger than current height,
                # indicating the current height could be propogated from
                # stack top position
                start = topI
                
            stack.append((start, height))
            
        # there is a chance that elements could still be left in teh stack
        # whose width would contribute till the end
        
        # print(stack, lra)
        
        for i, h in stack:
            lra = max(lra, h * (len(heights) - i))
            
        return lra