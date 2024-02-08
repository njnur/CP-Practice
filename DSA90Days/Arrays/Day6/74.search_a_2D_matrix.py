from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    """
    Leetcode problem link: https://leetcode.com/problems/search-a-2d-matrix/

    :param matrix: m x n integer matrix with the following two properties:
        Each row is sorted in non-decreasing order.
        The first integer of each row is greater than the last integer of the previous row.
    :param target: an integer
    :return: true if target is in matrix or false otherwise.
    """
    matrix_len = len(matrix)
    for i in range(0, matrix_len):
        if matrix[i][-1] == target:
            return True
        elif matrix[i][-1] > target:
            low = 0
            high = len(matrix[i]) - 1

            while low <= high:
                mid = (low + high) // 2
                if target > matrix[i][mid]:
                    low = mid + 1
                elif target < matrix[i][mid]:
                    high = mid - 1
                else:
                    return True
            return False

    return False


if __name__ == '__main__':
    print(search_matrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3))
    print(search_matrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13))
