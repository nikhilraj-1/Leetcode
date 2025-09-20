class Router:

    def __init__(self, memoryLimit: int):
        self.q = deque(maxlen = memoryLimit)
        self.memoryLimit = memoryLimit
        self.s = set()
        self.dest_map = defaultdict(list) 

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        item = (source, destination, timestamp)
        if item in self.s: 
            return False
        if len(self.q) >= self.memoryLimit:
            old = self.q.popleft()
            self.s.remove(old)
            os, od, ot = old
            
            idx = bisect_left(self.dest_map[od], ot)
            if idx < len(self.dest_map[od]) and self.dest_map[od][idx] == ot:
                self.dest_map[od].pop(idx)
            if not self.dest_map[od]:
                del self.dest_map[od]

        
        self.q.append(item)
        self.s.add(item)
        self.dest_map[destination].append(timestamp)  
        return True

        

    def forwardPacket(self) -> List[int]:
        if len(self.q)==0:
            return []
        item = self.q.popleft()
        self.s.remove(item)
        s, d, t = item
        idx = bisect_left(self.dest_map[d], t)
        if idx < len(self.dest_map[d]) and self.dest_map[d][idx] == t:
            self.dest_map[d].pop(idx)
        if not self.dest_map[d]:
            del self.dest_map[d]
        
        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dest_map:
            return 0
        ts_list = self.dest_map[destination]
        left = bisect_left(ts_list, startTime)
        right = bisect_right(ts_list, endTime)
        return right - left
            
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)