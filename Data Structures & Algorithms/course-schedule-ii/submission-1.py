class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []

        graph = [[] for _ in range(numCourses)]
        in_degrees = [0] * numCourses

        for prereq in prerequisites:
            course, preq = prereq[0], prereq[1]
            graph[preq].append(course)
            in_degrees[course] += 1

        queue = deque()
        for course in range(numCourses):
            if in_degrees[course] == 0:
                queue.append(course)

        course_taken = []
        while queue:
            curr_course = queue.popleft()
            course_taken.append(curr_course)
            
            for next_course in graph[curr_course]:
                in_degrees[next_course] -= 1
                if in_degrees[next_course] == 0:
                    queue.append(next_course)

        return course_taken if len(course_taken) == numCourses else []