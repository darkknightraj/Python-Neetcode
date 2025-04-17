def contains_duplicate(nums):
    nums.sort()  # Sort the list
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False

# Example usage
nums = [1, 2, 3, 4, 5, 2]

print(contains_duplicate(nums))  # Output: True
print(contains_duplicate([1,2,3,5]))   #Output : False
