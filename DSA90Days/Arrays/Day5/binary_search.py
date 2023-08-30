class BinarySearch:
    @staticmethod
    def iterative_method(input_arr: list, key: int) -> int:
        low = 0
        high = len(input_arr) - 1

        while low <= high:
            mid = (low + high) // 2
            if key > input_arr[mid]:
                low = mid + 1
            elif key < input_arr[mid]:
                high = mid - 1
            else:
                return mid

        return -1

    @staticmethod
    def recursive_method(input_arr: list, key: int, low: int = 0, high: int = None) -> int:
        if high is None:
            high = len(input_arr) - 1

        if high < low:
            return -1

        mid = (low + high) // 2
        if key == input_arr[mid]:
            return mid
        elif key > input_arr[mid]:
            return BinarySearch.recursive_method(input_arr, key, mid + 1, high)
        else:
            return BinarySearch.recursive_method(input_arr, key, low, mid - 1)


if __name__ == '__main__':
    input_array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    search_key = 91
    print(BinarySearch().iterative_method(input_arr=input_array, key=search_key))
    print(BinarySearch().recursive_method(input_arr=input_array, key=search_key, low=0, high=len(input_array)))
