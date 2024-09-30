class MinStack:
    def __init__(self):

    def push(self, val: int) -> None:

    def pop(self) -> None:

    def top(self) -> int:

    def get_min(self) -> int:


if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    obj.get_min()
    obj.pop()
    obj.top()
    obj.get_min()
