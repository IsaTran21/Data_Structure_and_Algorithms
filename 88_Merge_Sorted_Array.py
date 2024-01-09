def sorted_array(nums_1, nums_2, m, n):
    """ the first m elements denote the elements that should be merged
    and the last n elements are set and should be ignored
    nums2 has a length of n."""

    if m == 0:
        if n == 0:
            return []
        else:
            return nums_2
    new_arr = nums_1[:m]
    new_arr.extend(nums_2)
    bubble_sort(new_arr)
    return new_arr

def bubble_sort(arr):
    i = len(arr)
    while i >= 1:
        for j in range(i - 1):
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
        i = i - 1

    return arr

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(sorted_array(nums1, nums2,m,n))