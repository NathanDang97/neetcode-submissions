class Solution:
    # O(n * m) time, m: the number of tasks, n: the given idle time
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_heap = [cnt for cnt in counter.values()]
        heapq.heapify_max(max_heap)

        queue = deque() # pairs of [count, idleTime]

        time = 0
        while max_heap or queue:
            # process the most frequent task
            time += 1
            if max_heap:
                count = heapq.heappop_max(max_heap) - 1
                # if there are more of this task down the line
                # add it to the queue for furture processing
                if count > 0:
                    queue.append([count, time + n])
            
            # if there are more idle tasks
            # process the current most frequent one when it's ready
            if queue and queue[0][1] == time:
                heapq.heappush_max(max_heap, queue.popleft()[0])

        return time
