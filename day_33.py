from typing import List
class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2

            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1  # move right to find a closer timestamp
            else:
                r = m - 1  # move left to find a smaller timestamp

        return res

if __name__ == "__main__":
    timeMap = TimeMap()
    timeMap.set("foo", "bar", 1)
    print(timeMap.get("foo", 1))  # Output: "bar"
    print(timeMap.get("foo", 3))  # Output: "bar"
    timeMap.set("foo", "bar2", 4)
    print(timeMap.get("foo", 4))  # Output: "bar2"
    print(timeMap.get("foo", 5))  # Output: "bar2"