"""
Insertion Sort tutorial:
https://www.youtube.com/watch?v=gbJzL6IJig0
https://www.youtube.com/watch?v=oTICKmJhLXI
https://www.youtube.com/watch?v=enhpoXDWPcQ
"""
from typing import List


def insertion_sort(input_arr: List) -> List:
    for i in range(1, len(input_arr)):
        point_element = input_arr[i]
        for j in range(i-1, -1, -1):
            if input_arr[j] > point_element:
                input_arr[j+1] = input_arr[j]
                input_arr[j] = point_element

    return input_arr


if __name__ == '__main__':
    print(insertion_sort(input_arr=[9, 0, 5, 2, 6, 1]))
