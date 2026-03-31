class MyStack:

    #SELF IS AN OBJECT NOT A LIST!

    def __init__(self):
        self.data = [] #syntax error this is how to create a queue

    def push(self, x: int) -> None:
        self.data.append(x) #JUST ADD IT

    def pop(self) -> int:
        val = self.data[-1]
        self.data.pop(-1)
        return val #function exits after return!

    def top(self) -> int:
        return self.data[-1]

    def empty(self) -> bool:
        return True if not self.data else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()