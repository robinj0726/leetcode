# The time complexity of the `threeSum` function is O(n^2), where n is the length of the input array `nums`. This is because we have nested loops that iterate through the array, resulting in a quadratic time complexity.
# The space complexity of the `threeSum` function is O(log n), where n is the length of the input array `nums`. This is because we sort the array in place, which takes O(log n) space.
# The `threeSum` function takes an array of integers `nums` as input and returns a list of lists containing all unique triplets in the array which gives the sum of zero. If no such triplets are found, an empty list is returned.

def threeSum(nums):
    # Sort the array in ascending order
    nums.sort()
    
    # Initialize an empty list to store the triplets
    triplets = []
    
    # Iterate through the array, considering each element as the first element of the triplet
    for i in range(len(nums) - 2):
        # Skip duplicates to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Set the left and right pointers
        left = i + 1
        right = len(nums) - 1
        
        # Find the remaining two elements of the triplet
        while left < right:
            # Calculate the sum of the current triplet
            total = nums[i] + nums[left] + nums[right]
            
            # If the sum is zero, add the triplet to the result list
            if total == 0:
                triplets.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates to avoid duplicate triplets
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # Move the pointers towards the center
                left += 1
                right -= 1
            
            # If the sum is less than zero, move the left pointer to the right
            elif total < 0:
                left += 1
            
            # If the sum is greater than zero, move the right pointer to the left
            else:
                right -= 1
    
    return triplets

