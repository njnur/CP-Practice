from typing import List


class Solution:
    @staticmethod
    def max_area_bruteforce(height: List[int]) -> int:
        max_area = 0

        for index_1 in range(0, len(height)):
            for index_2 in range(1, len(height)):
                area = min(height[index_1], height[index_2]) * (index_2 - index_1)
                if area > max_area:
                    max_area = area

        return max_area

    @staticmethod
    def max_area_shifting_pointers(height: List[int]) -> int:
        max_area = 0
        first_index = 0
        last_index = len(height) - 1

        while last_index > first_index:
            area = min(height[first_index], height[last_index]) * (last_index - first_index)
            max_area = max(area, max_area)
            if height[last_index] >= height[first_index]:
                first_index += 1
            else:
                last_index -= 1

        return max_area


if __name__ == '__main__':
    # using bruteforce method
    print("Using bruteforce method:")
    print(Solution().max_area_bruteforce(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(Solution().max_area_bruteforce(height=[2, 3, 4, 5, 18, 17, 6]))
    print(Solution().max_area_bruteforce(height=[1, 1]))
    print(Solution().max_area_bruteforce(height=[1]))
    print(Solution().max_area_bruteforce(height=[]))

    # using shifting pointers method
    print("\nUsing shifting pointers method:")
    print(Solution().max_area_shifting_pointers(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(Solution().max_area_shifting_pointers(height=[2, 3, 4, 5, 18, 17, 6]))
    print(Solution().max_area_shifting_pointers(height=[1, 1]))
    print(Solution().max_area_shifting_pointers(height=[1]))
    print(Solution().max_area_shifting_pointers(height=[]))
