"""
  python implementation of Kth Largest item (Randomized Selection)
  Average Time Complexity: O(n)
"""
import random

def findKthLargest(nums, k):
    if (len(nums) == 1) or (len(set(nums)) == 1):
        return nums[0]

    nums_left, nums_right, pivot = partition(nums)

    if len(nums_right) == k - 1:
        return pivot

    if len(nums_right) >= k:
        result = findKthLargest(nums_right, k)
    else:
        result = findKthLargest(nums_left, k - len(nums_right))

    return result


def partition(array):
    pivot = random.choice(array)
    array_left = []
    array_right = []
    for i in range(len(array)):
        if array[i] > pivot:
            array_right.append(array[i])
        elif array[i] <= pivot:
            array_left.append(array[i])

    return array_left, array_right, pivot


if __name__ == '__main__':
    print(findKthLargest([3, 2, 1, 4, 5, 6, 1000], 2))
    print(findKthLargest([3, 2, 1, 4, 5, 6, 1000], 1))
    print(findKthLargest([3, 2, 1, 4, 5, 6, 1000], 3))
    print(findKthLargest([3, 2, 1, 4, 5, 6, -1], 7))
    print(findKthLargest([3, 3], 2))


