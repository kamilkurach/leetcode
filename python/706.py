class MyHashMap:

    def __init__(self):
        self.tab = []

    def put(self, key: int, value: int) -> None:
        try:
            for e in self.tab:
                if e[0] == key:
                    self.tab[self.tab.index(e)][1] = value
            self.tab.index([key, value])
        except ValueError:
            self.tab.append([key, value])

    def get(self, key: int) -> int:
        for e in self.tab:
            if e[0] == key:
                return e[1]
        return -1

    def remove(self, key: int) -> None:
        for e in self.tab:
            if e[0] == key:
                self.tab.pop(self.tab.index(e))


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
