"""
Problem Statement

You’re given a stack consisting of 'N' integers. Your task is to sort this stack in descending order using recursion.
We can only use the following functions on this stack S.

is_empty(S) : Tests whether the stack is empty or not.
push(S) : Adds a new element to the stack.
pop(S) : Removes a top element from the stack.
top(S) : Returns the value of the top element. Note that this function does not remove elements from the stack.

Note :
1) Use of any loop constructs like while, for etc., is not allowed.
2) The stack may contain duplicate integers.
3) The stack may contain any integer, i.e. it may either be negative, positive or zero.

Constraints:
1 <= 'T' <= 100
1 <=  'N' <= 100
1 <= |'V'| <= 10^9

Where |V| denotes the absolute value of any stack element.

Time limit: 1 sec

Sample Input 1:
1
5
5 -2 9 -7 3

Sample Output 1:
9 5 3 -2 -7

Explanation of Sample Input 1:
9 Is the largest element; hence, it’s present at the top. Similarly, 5>3, 3>-2, and -7 being the smallest element is present at the last.


Sample Input 2:
1
5
-3 14 18 -5 30

Sample Output 2:
30 18 14 -3 -5

Explanation of Sample Input 2:
30 is the largest element; hence, it’s present at the top. Similarly, 18>14, 14>-3, and -5, being the smallest element, is present at the last.
"""
from typing import List, Any


def is_empty(input_stack: List) -> bool:
    """
    Check if the stack is empty.

    Returns:
        bool: _description_
    """
    return len(input_stack) == 0

def push(input_stack: List, item: int) -> None:
    """
    Add an item to the top of the stack.

    Args:
        input_stack (List):
        item (Any): The item to be added to the stack.
    """
    input_stack.append(item)

def pop(input_stack: List) -> int:
    """
    Remove and return the item from the top of the stack.

    Raises:
        IndexError: If the stack is empty.
    """
    if is_empty(input_stack):
        raise IndexError("Can not pop from an empty stack")
    return input_stack.pop()

def top(input_stack: List) -> int:
    """
    Return the item at the top of the stack without removing it.

    Raises:
        IndexError: If the stack is empty.

    Returns:
        Int: The item at the top of the stack.
    """
    if is_empty(input_stack):
        raise IndexError("Can not peek an empty stack")
    return input_stack[-1]

def insert_in_sorted_stack(input_stack: List, item: int) -> List:
    if is_empty(input_stack) or top(input_stack) >= item:
        push(input_stack, item)
    else:
        temp = pop(input_stack)
        insert_in_sorted_stack(input_stack, item)
        push(input_stack, temp)


def sort_stack_using_recursion(input_list: List[int]) -> List[int]:
    if is_empty(input_list):
        return []
    else:
        temp = pop(input_list)
        sort_stack_using_recursion(input_list)
        insert_in_sorted_stack(input_list, temp)

    return input_list



if __name__ == '__main__':
    size:int = int(input())
    stack:List[int] = []
    for i in range(0, size):
        stack.append(int(input()))

    sorted_stack = sort_stack_using_recursion(stack)
    print(sorted_stack)
