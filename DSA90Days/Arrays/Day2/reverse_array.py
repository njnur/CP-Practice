from typing import List


def reverse_array(num_arr: List) -> List:
    """
    Reverse array with constant space complexity
    :param num_arr: input array
    :return: reversed array
    """
    arr_len = len(num_arr)
    last_index = arr_len - 1

    for i in range(0, arr_len):
        if i <= last_index - i:
            temp = num_arr[last_index - i]
            num_arr[last_index - i] = num_arr[i]
            num_arr[i] = temp
        else:
            break

    return num_arr


if __name__ == '__main__':
    arr = [3, 5, 9, 4, 2]

    print("Using custom function:")
    print(reverse_array(num_arr=arr))

    # one liner in python
    print("Using python one liner slicing:")
    print(arr[:: -1])
