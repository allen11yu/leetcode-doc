import collections


class TimeMap:

    def __init__(self):
        self.hashmap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.hashmap[key]

        res = ""
        l, r = 0, len(vals) - 1
        while l <= r:
            m = (l + r) // 2
            if timestamp >= vals[m][1]:
                l = m + 1
                res = vals[m][0]
            else:
                r = m - 1
        return res
