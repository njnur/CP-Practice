from typing import List, Any


class Solution:
    @staticmethod
    def two_sum_bruteforce(nums: List[int], target: int) -> Any:
        for num_1_index in range(0, len(nums)):
            for num_2_index in range(1, len(nums)):
                if target == nums[num_1_index] + nums[num_2_index]:
                    return [num_1_index, num_2_index]
        return None

    @staticmethod
    def two_sum_pointer_technique(nums: List[int], target: int) -> Any:
        for index_1 in range(0, len(nums)):
            num_to_find = target - nums[index_1]
            for index_2 in range(index_1+1, len(nums)):
                if num_to_find == nums[index_2]:
                    return [index_1, index_2]
        return None

    @staticmethod
    def two_sum_hash_map(nums: List[int], target: int) -> Any:
        hash_table = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_table:
                return i, hash_table[complement]
            else:
                hash_table[nums[i]] = i
        return None


if __name__ == '__main__':
    print(Solution().two_sum_bruteforce(
        nums=[2, 7, 11, 15],
        target=9
    ))
