class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # construct a directed graph
        # in-degrees prepresent the number of prereqs of a course
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
            # add curr_course to the list of course taken
            curr_course = queue.popleft()
            course_taken.append(curr_course)

            # process the courses that use the curr_course as prereq
            # and only add these courses to the queue once all of their
            # prereqs are satisfied
            for next_course in graph[curr_course]:
                in_degrees[next_course] -= 1
                if in_degrees[next_course] == 0:
                    queue.append(next_course)

        return True if len(course_taken) == numCourses else False

            
