def twoSum(nums, target):
    map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in map:
            return [map[complement], i]
        map[num] = i
    return []

# Example usage:
nums = [2, 7, 11, 15]
target = 13
result = twoSum(nums, target)
print(result)