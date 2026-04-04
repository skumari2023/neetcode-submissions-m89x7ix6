class TimeMap:

    def __init__(self):
        #key = key; val = (val, timestamp)
        self.count = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        #list can only take one argument
        self.count[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.count:
            return ""

        arr = self.count[key]

        l = 0
        r = len(arr) - 1
        res = ""

        while l <= r:
            mid = (l+r)//2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1  
        return res
        
