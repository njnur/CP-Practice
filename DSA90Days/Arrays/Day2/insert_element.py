from typing import List
from copy import copy


def insert_element_in_between_an_array(element: int, num_arr: List) -> List:
    """
    Inserts an element in between an array
    :param element:
    :param num_arr: input array
    :return: new array
    """
    temp_arr = []
    copy_arr = copy(num_arr)
    for i in range(0, len(num_arr)):
        if num_arr[i] == 9:
            temp_arr.append(9)
            temp_arr.append(element)
            break
        else:
            temp_arr.append(num_arr[i])
            copy_arr.pop(i)

    return temp_arr + copy_arr


if __name__ == '__main__':
    arr = [3, 5, 9, 4, 2]
    new_element = 101

    # add this element between 9 and 4
    print(insert_element_in_between_an_array(element=new_element, num_arr=arr))

    # # python one liner
    print("One liner solution:")
    arr.insert(arr.index(9) + 1, new_element)
    print(arr)
