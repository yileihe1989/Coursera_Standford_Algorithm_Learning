"""
  Compute count inversion using divide and conquer
  Time Complexity: O(nlogn)
"""

def count_split_inv(B, C):
    i, j = 0, 0
    Z = 0
    D = []
    while i < len(B) and j < len(C):
        D.append(min(B[i], C[j]))
        if B[i] < C[j]:
            i = i + 1
        else:
            Z += len(B[i:])
            j += 1

    if B[i:] or C[j:]:
        D.extend(B[i:] or C[j:])
    return D, Z


def sort_count(A):
    n = len(A)
    if n <= 1:
        return A, 0

    mid_point = int(n / 2)
    B, X = sort_count(A[:mid_point])
    C, Y = sort_count(A[mid_point:])
    D, Z = count_split_inv(B, C)
    return D, X + Y + Z

if __name__ == '__main__':
    f = open("IntegerArray.txt", "rt")
    array = [int(i.replace("\n", "")) for i in f]
    print(sort_count(array)[1])