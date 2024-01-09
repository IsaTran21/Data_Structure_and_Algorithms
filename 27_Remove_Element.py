def removeElement(nums: list[int], val: int) -> int:
    while True:
        temp = len(nums)

        for i in range(len(nums)):
            if nums[i] == val:
                nums[:] = nums[:i] + nums[i + 1:]
                break
        l = len(nums)
        if temp == l:
            break
    return len(nums)

nums = [3,2,2,3,4,4,2,2]
val = 3
print(removeElement(nums,val))