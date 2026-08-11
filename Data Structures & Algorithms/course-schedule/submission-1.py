from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        a, b : must a first and then b
        b -> a
        """

        # Kahn's algorithm
        # topological sort
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        # set start position
        queue = deque()
        for course, num in enumerate(indegree):
            if num == 0:
                queue.append(course)
    
        while queue:
            curr_course = queue.popleft()
            numCourses -= 1

            for next_course in graph[curr_course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)
        return numCourses == 0





