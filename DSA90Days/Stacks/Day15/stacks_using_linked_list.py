from typing import Any, Optional


class Node:
    """
    Class that serves as the building block for the linked list.
    """
    def __init__(self, data: Any, next: Optional['Node'] = None) -> None:
        self.data = data
        self.next = next


class StackUsingLinkedList:
    """
    This implementation provides a basic stack using linked List.
    """
    def __init__(self, head: Optional[Node] = None) -> None:
        self.head = head
    
    def is_empty(self) -> bool:
        """
        Check if the stack is empty.

        Returns:
            bool: 
        """
        return True if self.head is None else False

    def push(self, item: Any) -> None:
        """
        Add an item to the top of the stack.

        Args:
            item (Any): The item to be added to the stack.
        """
        new_node_obj = Node(data=item)

        if self.is_empty():
            self.head = new_node_obj
            return
        
        last_head_obj = self.head
        while last_head_obj.next:
            last_head_obj = last_head_obj.next
        last_head_obj.next = new_node_obj
        
    def pop(self) -> None:
        """
        Remove and return the item from the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Can not pop from an empty stack")

        current_node = self.head
        while current_node:
            if current_node.next.next is None:
                current_node.next = None
                break
            current_node = current_node.next

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

        current_node = self.head
        while current_node:
            if current_node.next is None:
                return current_node.data
            current_node = current_node.next

    def __str__(self) -> str:
        display_elements = []
        current_node = self.head

        while current_node:
            display_elements.append(str(current_node.data))
            current_node = current_node.next

        if display_elements:
            return ' ==> '.join(display_elements)
        return 'Empty'


if __name__ == "__main__":
    stack_obj = StackUsingLinkedList()

    print("Before Pushing: " + str(stack_obj))
    print("Check if the stack is empty: " + str(stack_obj.is_empty()))

    stack_obj.push(1)
    stack_obj.push(2)
    stack_obj.push(3)

    print("\nAfter Pushing: " + str(stack_obj))
    print("Check if the stack is empty: " + str(stack_obj.is_empty()))

    stack_obj.pop()
    print("\nAfter Popping: " + str(stack_obj))

    print("Peeking the Stack: " + str(stack_obj.peek()))
    print("Check if the stack is empty: " + str(stack_obj.is_empty()))
