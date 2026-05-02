class TimeMap:

    def __init__(self):
        self.dt = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dt[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.dt[key])
        while l < r:
            m = (l + r) >> 1
            if self.dt[key][m][0] > timestamp: 
                r = m
            else:
                l = m + 1
        
        if r == 0:
            return ""
        
        return self.dt[key][r - 1][1]