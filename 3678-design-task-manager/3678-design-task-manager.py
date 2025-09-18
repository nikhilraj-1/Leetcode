class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_map = {}
        self.pq = []
        for i,t,p in tasks:
            self.add(i,t,p)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_map[taskId] = (userId,priority)
        heapq.heappush(self.pq,(-priority,-taskId))
        

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.task_map[taskId]
        self.task_map[taskId] = (userId,newPriority)
        heapq.heappush(self.pq, (-newPriority, -taskId))
        

    def rmv(self, taskId: int) -> None:
        del self.task_map[taskId]

    def execTop(self) -> int:
        while self.pq:
            p,t = heapq.heappop(self.pq)
            if -t in self.task_map:
                i,cp= self.task_map[-t]
                if cp == -p:
                    self.rmv(-t)
                    return i
        return -1



        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()