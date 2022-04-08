from typing import List


class Solution:
    @staticmethod
    def trapping_rainwater_bruteforce(height: List[int]) -> int:
        max_unit = 0
        max_left = 0
        max_right = 0

        for item in range(1, len(height)):
            for pointer in range(0, len(height)):
                if item > pointer:
                    if height[pointer] > max_right:
                        max_right = height[pointer]
                elif item < pointer:
                    if height[pointer] > max_left:
                        max_left = height[pointer]

            water_unit = min(max_left, max_right) - height[item]

            if water_unit > 0:
                max_unit = max_unit + water_unit

        return max_unit

    @staticmethod
    def trapping_rainwater_optimal(height: List[int]) -> int:
        max_area = 0

        return max_area


if __name__ == '__main__':
    # using bruteforce method
    print("Using bruteforce method:")
    print(Solution().trapping_rainwater_bruteforce(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    # print(Solution().trapping_rainwater_bruteforce(height=[4, 2, 0, 3, 2, 5]))
    # print(Solution().trapping_rainwater_bruteforce(height=[2, 3, 2]))
    # print(Solution().trapping_rainwater_bruteforce(height=[1, 1]))
    # print(Solution().trapping_rainwater_bruteforce(height=[1]))
    # print(Solution().trapping_rainwater_bruteforce(height=[]))

    # using shifting pointers method
    # print("\nUsing optimal method:")
    # print(Solution().trapping_rainwater_optimal(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    # print(Solution().trapping_rainwater_optimal(height=[4, 2, 0, 3, 2, 5]))
    # print(Solution().trapping_rainwater_optimal(height=[2, 3, 2]))
    # print(Solution().trapping_rainwater_optimal(height=[1, 1]))
    # print(Solution().trapping_rainwater_optimal(height=[1]))
    # print(Solution().trapping_rainwater_optimal(height=[]))
