class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # a map to store crses and respective preRequisistes.
        crs_preReq_map = {crsNum: list() for crsNum in range(numCourses)}
        
        # creating a adjacency list
        for crs, preReq in prerequisites:
            crs_preReq_map[crs].append(preReq)
            
        visit_set = set()
        cycle_set = set()
        output_crs = []
        
        def dfs(crs):
            # if crs in cycle_set:
            if crs in cycle_set:
                # cycle detected
                return False
            # a crs has been fully visited and it can be taken
            if crs in visit_set:
                return True
            
            # add a crs to cycle 
            cycle_set.add(crs)
            for prereq in crs_preReq_map[crs]:
                # check the output of dfs for this course
                if not dfs(prereq):
                    return False
            # if no cycles detected
            # this indicates the courses can be taken without any issue
            cycle_set.remove(crs)
            # a visited course can be taken
            visit_set.add(crs)
            # adding the crs to the output
            output_crs.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                # if any cycle detected returning []
                return []
        return output_crs