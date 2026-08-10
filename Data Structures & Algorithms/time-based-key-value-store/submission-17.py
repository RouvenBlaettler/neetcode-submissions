class TimeMap:

    def __init__(self):
        self.db = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.db.keys():
            self.db[key] = [[value, timestamp]]
        else:
            self.db[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.db:
            return ""
        arr = self.db[key]
        l, r = 0, len(arr)-1
        closest = 0
        
        while l <= r:
            m = (l+r)//2
            if arr[m][1] == timestamp:
                return arr[m][0]
            elif arr[m][1] < timestamp:
                closest = arr[m][0]
                l = m+1
            else:
                r = m-1
        return closest if closest else ""


        
