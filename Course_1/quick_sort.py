"""
  python implementation of quick sort
  Average Time Complexity: O(nlogn)

  1) how to prove 1/2 + 1/3 + 1/4 + ... + 1/n < logn
  2) how to prove the average time complexity is O(nlogn) under the circumstances that master theorem is not applicable?
"""
from random import randint


def partition(nums, pivot_index):
    pivot = nums[pivot_index]

    latest_left = -1
    for i in range(len(nums)):
        if nums[i] < pivot:
            latest_left += 1
            if latest_left == pivot_index:
                latest_left += 1
            nums[latest_left], nums[i] = nums[i], nums[latest_left]

    if latest_left == -1:
        return [], nums[:pivot_index] + nums[pivot_index + 1:], [pivot]

    if latest_left > pivot_index:
        nums[latest_left], nums[pivot_index] = nums[pivot_index], nums[latest_left]
    elif latest_left < pivot_index:
        latest_left += 1
        nums[latest_left], nums[pivot_index] = nums[pivot_index], nums[latest_left]
    return nums[:latest_left], nums[latest_left + 1:], [pivot]


def quick_sort(nums):
    if len(nums) > 1:
        pivot_index = randint(0,len(nums)-1)
        left_nums, right_nums, pivot = partition(nums,pivot_index)
        left_array = quick_sort(left_nums)
        right_array = quick_sort(right_nums)
        return left_array + pivot + right_array
    else:
        return nums


if __name__ == '__main__':
    print (quick_sort([3,5,1,0,190,23]))
    print (quick_sort([1,2,3,4,5]))
    print (quick_sort([100,99,88,77]))
    print (quick_sort([7,9,1,10,3,29]))