from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        a,b: b first -> a later

        course label: 0 ~ numCourses-1
        """
        # kahn's algorithm - topological sort
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        course_order = []
        while queue:
            curr_course = queue.popleft()
            course_order.append(curr_course)

            for next_course in graph[curr_course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)
        
        return course_order if len(course_order) == numCourses else []