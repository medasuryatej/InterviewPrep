class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # a map to store crses and respective preRequisistes.
        crs_preReq_map = {crsNum: list() for crsNum in range(numCourses)}
        
        # creating a adjacency list
        for crs, preReq in prerequisites:
            crs_preReq_map[crs].append(preReq)
            
        visit_set = set()
        
        def dfs(crs):
            # if crs in visit_set:
            if crs in visit_set:
                # cycle detected
                return False
            if crs_preReq_map[crs] == []:
                # no prereqs for a course
                return True
            
            visit_set.add(crs)
            for prereq in crs_preReq_map[crs]:
                # check the output of dfs for this course
                if not dfs(prereq):
                    return False
            # if no cycles detected
            # this indicates the courses can be taken without any issue
            visit_set.remove(crs)
            # resetting the prereqs of a course 
            # because we determined that a course can be taken
            crs_preReq_map[crs] = []
            
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True