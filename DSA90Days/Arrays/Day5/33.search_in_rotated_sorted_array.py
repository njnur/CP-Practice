class Solution:
    """
    Leetcode problem solution of https://leetcode.com/problems/search-in-rotated-sorted-array/
    """
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[low]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1


if __name__ == '__main__':
    print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
    print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
    print(Solution().search(nums=[], target=3))
    print(Solution().search(nums=[1], target=0))
