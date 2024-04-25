def removeDuplicates(nums):
    index = 1
    for i in range(len(nums) - 1):
        if nums[i] != nums[i + 1]:
            nums[index] = nums[i + 1]
            index += 1
    return index

print(removeDuplicates([1,1,2])) # 2
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # 5