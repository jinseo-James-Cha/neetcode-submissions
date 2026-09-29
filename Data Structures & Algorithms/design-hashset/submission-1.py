class MyHashSet:
    def __init__(self):
        self.data = [False] * 1000001

    def add(self, key: int) -> None:
        self.data[key] = True

    def remove(self, key: int) -> None:
        self.data[key] = False

    def contains(self, key: int) -> bool:
        return self.data[key]

    # O(n) soltution with array
    # def __init__(self):
    #     self.data = []

    # def add(self, key: int) -> None:
    #     if key not in self.data:
    #         self.data.append(key)

    # def remove(self, key: int) -> None:
    #     if key in self.data:
    #         self.data.remove(key)

    # def contains(self, key: int) -> bool:
    #     return key in self.data
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)