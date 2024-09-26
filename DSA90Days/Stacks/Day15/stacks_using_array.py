from typing import Any


class StackUsingArray:
    """
    This implementation provides a basic stack using Python’s list structure as an array.
    """
    def __init__(self) -> None:
        self.stack = []
    
    def is_empty(self) -> bool:
        """
        Check if the stack is empty.

        Returns:
            bool: _description_
        """
        return len(self.stack) is 0

    def push(self, item: Any) -> None:
        """
        Add an item to the top of the stack.

        Args:
            item (Any): The item to be added to the stack.
        """
        self.stack.append(item)
    
    def pop(self) -> None:
        """
        Remove and return the item from the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Can not pop from an empty stack")
        return self.stack.pop()

    def peek(self) -> Any:
        """
        Return the item at the top of the stack without removing it.

        Raises:
            IndexError: If the stack is empty.

        Returns:
            Any: The item at the top of the stack.
        """
        if self.is_empty():
            raise IndexError("Can not peek an empty stack")
        return self.stack[-1]

    def __str__(self) -> str:
        return f"{self.stack}"


if __name__ == "__main__":
    stack_obj = StackUsingArray()
    print("Before Pushing: " + str(stack_obj) + "\n")
    stack_obj.push(1)
    stack_obj.push(2)
    stack_obj.push(3)
    print("After Pushing: " + str(stack_obj) + "\n")

    stack_obj.pop()
    print("After Popping: " + str(stack_obj) + "\n")

    print("Peeking the Stack: " + str(stack_obj.peek()) + "\n")
    print("Check if the stack is empty: " + str(stack_obj.is_empty()) + "\n")
