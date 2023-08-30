from typing import List


class Sort:
    """
    Tutorial
    https://www.youtube.com/watch?v=6pV2IF0fgKY&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=33
    https://www.youtube.com/watch?v=mB5HXBb_HY8&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=34
    https://www.youtube.com/watch?v=ak-pz7tS5DE&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=35
    """
    def merge_sort(self, input_array: List) -> List:
        low = 1
        high = len(input_array)
        mid = int((low + high) / 2)

        return self.merge(low=low, high=high, mid=mid)

    @staticmethod
    def merge(low: int, high: int, mid: int) -> List:
        """
        Two-way merging of array
        :return: Merged array
        """







        return


if __name__ == '__main__':
    print(Sort().merge_sort(input_array=[9, 0, 2, 6, 1]))
