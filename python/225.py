class MyStack:

    def __init__(self):
        self.arr = []

    def push(self, x: int) -> None:
        self.arr.insert(0, x)

    def pop(self) -> int:
        e = self.arr[0]
        self.arr = self.arr[1:]
        return e

    def top(self) -> int:
        return self.arr[0]
        
    def empty(self) -> bool:
        if len(self.arr) == 0:
            return True
        else:
            return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
