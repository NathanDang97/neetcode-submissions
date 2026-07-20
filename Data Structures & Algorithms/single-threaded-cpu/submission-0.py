class Solution:
    # sorting + min-heap solution, O(nlogn) time, O(n) space
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # attach the original index to each task
        for i, t in enumerate(tasks):
            t.append(i)
        # sort the tasks by enqueue time
        tasks.sort(key=lambda t: t[0])

        order, min_heap = [], [] # order is the result list
        i, curr_time = 0, tasks[0][0] # initialize the current time to the first task's enqueue time

        # use index i to track which tasks have been considered 
        # repeat the following process while some tasks still remain unprocessed or the min heap is not empty
        while min_heap or i < len(tasks):
            # add all tasks with enqueue time at or before the current time to the min heap
            while i < len(tasks) and curr_time >= tasks[i][0]:
                heapq.heappush(min_heap, [tasks[i][1], tasks[i][2]])
                i += 1
            # if the heap is empty, jump to the next task's enqueue time
            if not min_heap:
                curr_time = tasks[i][0]
            # otherwise, pop the task with the shortest processing time, update the current time, and add the index to the order list
            else:
                process_time, idx = heapq.heappop(min_heap)
                curr_time += process_time
                order.append(idx)

        return order