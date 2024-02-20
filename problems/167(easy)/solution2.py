def twoSum(numbers, target):
    # Initialize two pointers, one at the beginning and one at the end of the array
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        # Calculate the sum of the current left and right elements
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            # If the sum is equal to the target, return the indices (1-based) of the two numbers
            return [left + 1, right + 1]
        elif current_sum < target:
            # If the sum is less than the target, move the left pointer to the right
            left += 1
        else:
            # If the sum is greater than the target, move the right pointer to the left
            right -= 1
    
    # If no solution is found, return an empty list
    return []