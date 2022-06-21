class SolutionTLE:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # TLE
        def recursion(heights, curIndex, bricksLeft, laddersLeft):
            while curIndex < (len(heights)-2):
                if heights[curIndex] >= heights[curIndex+1]:
                    curIndex += 1
                else:
                    break
            # base case (reached end or no more bricks and no more ladders)
            if (curIndex == len(heights)-1) or  (bricksLeft == 0 and laddersLeft == 0):
                return curIndex
            
            maxReachableBIndex = curIndex
            maxReachableLIndex = curIndex
            # maxReachableIndex = curIndex
            
            diff = (heights[curIndex+1] - heights[curIndex])
            if bricksLeft >= diff:
                maxReachableBIndex = recursion(heights, curIndex+1, bricksLeft - diff, laddersLeft)
            if laddersLeft > 0:
                maxReachableLIndex = recursion(heights, curIndex+1, bricksLeft, laddersLeft-1)
            return max(maxReachableBIndex, maxReachableLIndex)
        
        return recursion(heights, 0, bricks, ladders)
    
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder_allocations = [] # We'll use heapq to treat this as a min-heap.
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            # If this is actually a "jump down", skip it.
            if climb <= 0:
                continue
            # Otherwise, allocate a ladder for this climb.
            heapq.heappush(ladder_allocations, climb)
            # If we haven't gone over the number of ladders, nothing else to do.
            if len(ladder_allocations) <= ladders:
                continue
            # Otherwise, we will need to take a climb out of ladder_allocations
            bricks -= heapq.heappop(ladder_allocations)
            # If this caused bricks to go negative, we can't get to i + 1
            if bricks < 0:
                return i
        # If we got to here, this means we had enough to cover every climb.
        return len(heights) - 1