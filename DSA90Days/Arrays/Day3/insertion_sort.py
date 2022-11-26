from typing import List


def insertion_sort(input_arr: List) -> List:
    for i in range(1, len(input_arr)):
        for j in range(i, 0, -1):
            point_element = input_arr[i]
            if input_arr[j-1] > point_element:
                input_arr[i] = input_arr[j-1]

    return input_arr


if __name__ == '__main__':
    print(insertion_sort(input_arr=[9, 0, 5, 2, 6, 1]))
