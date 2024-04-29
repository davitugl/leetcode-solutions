def searchInsert(nums, target):
    for i in range(len(nums)):
        if target <= nums[i]:
            return i
    return len(nums)


print(searchInsert([1,3,5,6], 5)) # 2
print(searchInsert([1,3,5,6], 2)) # 1
print(searchInsert([1,3,5,6], 7)) # 4
