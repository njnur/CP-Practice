## Binary Search Algorithm

Binary search is a commonly used algorithm for efficiently locating a specific element within a sorted collection (such
as an array) by repeatedly dividing the search interval in half. This algorithm significantly reduces the number of
comparisons required to find the desired element, making it much faster than linear search, especially for large
datasets.

### Requirements

- The collection must be sorted in ascending (or descending) order. This sorting is essential for the algorithm's
  effectiveness.
- Binary search works best with random access structures like arrays, where you can directly access elements using an
  index.

### Algorithm Steps

1. **Initialization**:
    - Set two pointers: `left` at the beginning of the collection and `right` at the end.
    - Calculate the middle index as `middle = (left + right) / 2`.

2. **Comparison**:
    - Compare the element at the middle index with the target value.
    - If the element is equal to the target, the search is successful, and the index of the element is returned.
    - If the element is less than the target, it means the target must be in the right half of the collection.
      Update `left = middle + 1` to narrow the search range.
    - If the element is greater than the target, it means the target must be in the left half of the collection.
      Update `right = middle - 1` to narrow the search range.

3. **Repetition**:
    - Repeat steps a and b until `left` is greater than `right`. This indicates that the search interval has become
      empty, and the target element is not present in the collection.

### Complexity

- Binary search reduces the search space by half in each step, so it has a time complexity of O(log n), where n is the
  number of elements in the collection.
- This is significantly faster than linear search, which has a time complexity of O(n) in the worst case.

### Advantages

- Binary search is highly efficient for large datasets due to its logarithmic time complexity.
- It works particularly well for arrays and other random access data structures.

### Limitations

- The collection must be sorted, which requires preprocessing if the collection is not initially sorted.
- Binary search may not be suitable for data structures with slow random access, such as linked lists, as it relies on
  the ability to access elements quickly based on their index.

### Variations

- There are variations of binary search, such as binary search trees for dynamic data, and lower_bound/upper_bound
  binary searches for finding the insertion point of an element in a sorted collection.

### Video Tutorial
[Iterative Method](https://www.youtube.com/watch?v=C2apEw9pgtw&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=30)  
[Recursive Method](https://www.youtube.com/watch?v=uEUXGcc2VXM&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=31)

---

## Binary Search Example

Let's go through an example of using the binary search algorithm to find the index of a target element within a sorted
array.

### Given Data

Sorted Array: `[2, 5, 8, 12, 16, 23, 38, 56, 72, 91]`
Target Element: `23`

### Algorithm Steps

1. **Initialization**:
    - `left` = 0 (index of the first element)
    - `right` = 9 (index of the last element)
    - Calculate the middle index: `middle` = `(0 + 9) / 2 = 4`.

2. **Comparison**:
    - Compare `arr[4]` (element at index 4) with the target value `23`.
    - `arr[4]` = 16, which is less than 23.
    - Since the target value is greater, update `left` to `middle + 1` = 5.

3. **Repetition**:
    - Calculate the new middle index: `middle` = `(5 + 9) / 2 = 7`.

4. **Comparison**:
    - Compare `arr[7]` (element at index 7) with the target value `23`.
    - `arr[7]` = 56, which is greater than 23.
    - Since the target value is smaller, update `right` to `middle - 1` = 6.

5. **Repetition**:
    - Calculate the new middle index: `middle` = `(5 + 6) / 2 = 5`.

6. **Comparison**:
    - Compare `arr[5]` (element at index 5) with the target value `23`.
    - `arr[5]` = 23, which is equal to the target value!
    - The search is successful, and the index 5 is returned.

### Summary

- Step 1: Initial `left` = 0, `right` = 9, `middle` = 4
- Step 2: Updated `left` = 5, `middle` = 7
- Step 3: Updated `right` = 6, `middle` = 5
- Step 4: Found target value at index 5

---

### Time Complexity:

The time complexity of an algorithm represents how its runtime grows as the input size increases. In the case of binary
search:

- In each step, the search interval is divided in half, effectively reducing the search space by half.
- This means that in the worst case, the algorithm needs to repeat this process until the search interval becomes
  empty (i.e., `left` exceeds `right`).
- The number of times the search interval can be divided by 2 until it becomes empty can be roughly described as the
  number of times you can divide the initial size of the array until it becomes 1.

Mathematically, if the initial size of the array is `n`, then the number of steps `k` required to reduce it to 1 is
approximately `log2(n)`, where `log2` is the logarithm base 2.

Hence, the time complexity of binary search is **O(log n)**.

### Space Complexity:

The space complexity of an algorithm refers to the amount of memory used by the algorithm. In the case of binary search:

- The algorithm requires only a few variables to keep track of the indices (`left`, `right`, and `middle`).
- These variables don't depend on the size of the input data but rather on the number of divisions performed during the
  search.

Therefore, the space complexity of binary search is **O(1)**, also known as constant space complexity.

### Summary:

- Time Complexity: **O(log n)** - The algorithm's efficiency comes from its ability to reduce the search space by half
  in each step, resulting in a logarithmic growth in runtime as the input size increases.
- Space Complexity: **O(1)** - The algorithm uses a constant amount of memory, regardless of the size of the input data.
