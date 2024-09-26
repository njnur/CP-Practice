## Longest Common Subsequence (LCS)

The Longest Common Subsequence (LCS) problem is a classic computer science problem, which is the task of finding the
longest subsequence common to all sequences in a set of sequences (often just two sequences). A subsequence is a
sequence that appears in the same relative order, but not necessarily contiguous. LCS is a foundational concept in the
fields of data comparison, bioinformatics, and in algorithms for version control, diff tools, and text editing.

#### Mathematical Formulation

Given two sequences `X = [x_1, x_2, ..., x_m]` and `Y = [y_1, y_2, ..., y_n]`, we aim to find a maximum-length
sequence `Z = [z_1, z_2, ..., z_k]` that is a subsequence of both `X` and `Y`.

The length of the longest common subsequence can be defined recursively as follows:

1. If `X` or `Y` is empty, `LCS(X, Y) = 0`.
2. If `x_m = y_n`, then `LCS(X, Y) = 1 + LCS(X_{m-1}, Y_{n-1})`.
3. Otherwise, `LCS(X, Y) = max(LCS(X_{m-1}, Y), LCS(X, Y_{n-1}))`.

#### Dynamic Programming Approach

A dynamic programming approach is commonly used to solve the LCS problem efficiently by storing the results of
subproblems to avoid redundant computations.

Let `L[i][j]` be the length of the LCS of the sequences `X[1..i]` and `Y[1..j]`. The dynamic programming formula is as
follows:

- If `i = 0` or `j = 0`, `L[i][j] = 0`.
- If `x_i = y_j`, then `L[i][j] = L[i-1][j-1] + 1`.
- Otherwise, `L[i][j] = max(L[i-1][j], L[i][j-1])`.

#### Example

Consider two sequences X = "AGGTAB" and Y = "GXTXAYB".

- **Step 1**: Start with the first character of both sequences.
- **Step 2**: Compare and proceed through the sequences.
  - **Step 3**: Use dynamic programming to fill a table `L` where `L[i][j]` represents the length of LCS of `X[1..i]`
    and `Y[1..j]`.

The filled table `L` would help us find that the length of the LCS is 4. The LCS is "GTAB".

#### Implementation Example

Here's a Python function that implements the dynamic programming solution for LCS:

```python
def lcs(X, Y):
    m, n = len(X), len(Y)
    L = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L[m][n]


# Example usage
X = "AGGTAB"
Y = "GXTXAYB"
print(f"Length of LCS is {lcs(X, Y)}")
```

This example demonstrates how to calculate the length of the LCS. To reconstruct the actual subsequence, you would trace
back from `L[m][n]` through the matrix, moving in the direction that shows the increase in length, indicative of a match
in the sequence.