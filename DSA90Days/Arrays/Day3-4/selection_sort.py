from typing import List


class Sort:
    """
    Tutorial
    https://www.youtube.com/watch?v=9oWd4VJOwr0
    Complexity Analysis: https://www.khanacademy.org/computing/computer-science/algorithms/sorting-algorithms/a/analysis-of-selection-sort
    """
    def selection_sort(self, input_array: List) -> List:
        for index, elements in enumerate(input_array):
            if len(input_array) > index+1:
                min_index = self.minimum_values_index_in_the_sub_array(sub_array=input_array[index+1:]) + \
                            len(input_array[:index+1])
                if index+1 != min_index:
                    # swap elements of the two indexes
                    temp = input_array[index]
                    input_array[index] = input_array[min_index]
                    input_array[min_index] = temp

        return input_array

    @staticmethod
    def minimum_values_index_in_the_sub_array(sub_array: List) -> int:
        """
        finds the minimum value in the array and returns the index
        :param sub_array: the sub array to input
        :return: index of the minimum value in the subarray
        """
        min_val = sub_array[0]
        for index, element in enumerate(sub_array):
            if element < min_val:
                min_val = element

        return sub_array.index(min_val)


if __name__ == '__main__':
    print(Sort().selection_sort(input_array=[9, 0, 2, 6, 1]))
