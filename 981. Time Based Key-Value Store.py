class TimeMap:
    """
    SOLUTION1: Brute force (TLE)
    create dict store key: {timestamp: [v]}
    TIME: set O(1), get O(m)
    SPACE: O(n*m), n is number of key, m is number of timestamps
    """
    def __init__(self):
        self.dic = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        # key not exist, create new entry
        if key not in self.dic:
            self.dic[key] = {}
        # timestamp not exist, create new netry
        if timestamp not in self.dic[key]:
            self.dic[key][timestamp] = []
        # both exist, update val
        self.dic[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        # return value with time <= timestamp, nearest timestamp
        if key not in self.dic:
            return ""
        time = timestamp
        while time > 0:
            if time not in self.dic[key]:
                time -= 1
            else:
                # found max time 
                return self.dic[key][time][-1]
        return ""

    """
    SOLUTION2: Binary search
    create dict store key: [v, timestamp]}
    TIME: set O(1), get O(logn)
    SPACE: O(n*m), n is number of key, m is number of timestamps
    """
    def __init__(self):
        self.dic = collections.defaultdict(list) # key: [val, timestamp]
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        # timestamp is increasing , so set always add new entry instead of modify value
        self.dic[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # return value with time <= timestamp, nearest timestamp
        if key not in self.dic:
            return ""
        # now values is list [[v1, t1], [v2, t2], [v1, t3]]
        # time is increasing, so we need to find the time <= and cloest to timestamp
        values = self.dic[key]
        left, right = 0, len(values)-1
        res = ""

        while left <= right:
            mid = (left+right)//2
            if values[mid][1] <= timestamp:
                # mark now, but still find larger one
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)