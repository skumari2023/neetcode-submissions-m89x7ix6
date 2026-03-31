class MyQueue:

    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        val = int(len(self.data))* -1 
        value = self.data[val]
        self.data.pop(val)
        return value 

    def peek(self) -> int:
        val = self.data[int(len(self.data))* -1] 
        return val 
        

    def empty(self) -> bool:
        return True if not self.data else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()