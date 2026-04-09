class TimeMap:

    def __init__(self):
        self.count = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.count[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:

        if key not in self.count:
            return ""
        
        arr = self.count[key]

        l = 0 
        r = len(arr)

        while l < r:
            mid = (l+r)//2
            if arr[mid][0] <= timestamp:
                l = mid + 1
            else:
                r = mid
        
        #doing bisect right must check for bounds
        if l == 0:
            return ""

        return arr[l-1][1]
        
